import os
from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from werkzeug.utils import secure_filename
from app.models import Expense, Category, User
from app import db
from datetime import datetime
from flask_login import current_user, login_required

expenses_bp = Blueprint('expenses', __name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'pdf'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_default_user():
    user = User.query.first()
    if not user:
        user = User(username='admin', password_hash='pbkdf2:sha256:default_hash_for_testing', role='Admin')
        db.session.add(user)
        db.session.commit()
    return user

@expenses_bp.route('/')
@login_required
def index():
    # Search and Filter parameters
    search_query = request.args.get('search', '')
    category_id = request.args.get('category', '')
    payment_method = request.args.get('payment_method', '')
    
    query = Expense.query
    
    if search_query:
        query = query.filter(
            (Expense.title.like(f'%{search_query}%')) | 
            (Expense.description.like(f'%{search_query}%'))
        )
    
    if category_id:
        query = query.filter_by(category_id=int(category_id))
        
    if payment_method:
        query = query.filter_by(payment_method=payment_method)
        
    expenses = query.order_by(Expense.expense_date.desc()).all()
    categories = Category.query.all()
    
    # Ensure there are categories
    if not categories:
        default_cats = ['Electricity', 'Salaries', 'Transport', 'Stationery', 'Internet', 'Water Bills', 'Maintenance', 'Furniture', 'Events', 'Miscellaneous']
        for cat_name in default_cats:
            db.session.add(Category(name=cat_name))
        db.session.commit()
        categories = Category.query.all()
        
    return render_template('expenses/index.html', expenses=expenses, categories=categories, search_query=search_query, selected_category=category_id, selected_payment_method=payment_method, datetime=datetime)

@expenses_bp.route('/add', methods=['POST'])
@login_required
def add():
    title = request.form.get('title')
    description = request.form.get('description', '')
    
    try:
        amount_val = request.form.get('amount')
        if not amount_val:
            raise ValueError
        amount = float(amount_val)
        if amount < 0:
            raise ValueError
    except ValueError:
        flash('Invalid amount entered.', 'danger')
        return redirect(url_for('expenses.index'))

    category_id = int(request.form.get('category_id'))
    payment_method = request.form.get('payment_method')
    date_str = request.form.get('expense_date')
    
    expense_date = datetime.strptime(date_str, '%Y-%m-%d').date() if date_str else datetime.utcnow().date()
    
    # Handle receipt upload
    receipt_path = None
    if 'receipt' in request.files:
        file = request.files['receipt']
        if file and file.filename != '' and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            upload_folder = os.path.join(current_app.root_path, 'static', 'uploads')
            if not os.path.exists(upload_folder):
                os.makedirs(upload_folder)
            
            # Save file
            unique_filename = f"{datetime.utcnow().strftime('%Y%m%d%H%M%S')}_{filename}"
            file.save(os.path.join(upload_folder, unique_filename))
            receipt_path = f"uploads/{unique_filename}"

    # Determine creator
    creator = current_user if current_user.is_authenticated else get_default_user()
    
    expense = Expense(
        title=title,
        description=description,
        amount=amount,
        category_id=category_id,
        payment_method=payment_method,
        expense_date=expense_date,
        receipt_path=receipt_path,
        created_by=creator.id
    )
    
    db.session.add(expense)
    db.session.commit()
    flash('Expense added successfully!', 'success')
    return redirect(url_for('expenses.index'))

@expenses_bp.route('/edit/<int:id>', methods=['POST'])
@login_required
def edit(id):
    expense = Expense.query.get_or_404(id)
    
    if expense.created_by != current_user.id and current_user.role != 'Admin':
        flash('Unauthorized access!', 'danger')
        return redirect(url_for('expenses.index'))

    expense.title = request.form.get('title')
    expense.description = request.form.get('description', '')
    
    try:
        amount_val = request.form.get('amount')
        if not amount_val:
            raise ValueError
        amount = float(amount_val)
        if amount < 0:
            raise ValueError
        expense.amount = amount
    except ValueError:
        flash('Invalid amount entered.', 'danger')
        return redirect(url_for('expenses.index'))

    expense.category_id = int(request.form.get('category_id'))
    expense.payment_method = request.form.get('payment_method')
    
    date_str = request.form.get('expense_date')
    if date_str:
        expense.expense_date = datetime.strptime(date_str, '%Y-%m-%d').date()
        
    # Handle receipt upload if a new one is selected
    if 'receipt' in request.files:
        file = request.files['receipt']
        if file and file.filename != '' and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            upload_folder = os.path.join(current_app.root_path, 'static', 'uploads')
            if not os.path.exists(upload_folder):
                os.makedirs(upload_folder)
            
            # Save file
            unique_filename = f"{datetime.utcnow().strftime('%Y%m%d%H%M%S')}_{filename}"
            file.save(os.path.join(upload_folder, unique_filename))
            expense.receipt_path = f"uploads/{unique_filename}"

    db.session.commit()
    flash('Expense updated successfully!', 'success')
    return redirect(url_for('expenses.index'))

@expenses_bp.route('/delete/<int:id>', methods=['POST'])
@login_required
def delete(id):
    expense = Expense.query.get_or_404(id)
    
    if expense.created_by != current_user.id and current_user.role != 'Admin':
        flash('Unauthorized access!', 'danger')
        return redirect(url_for('expenses.index'))
    
    # Try deleting the receipt file if it exists
    if expense.receipt_path:
        filepath = os.path.join(current_app.root_path, 'static', expense.receipt_path)
        if os.path.exists(filepath):
            try:
                os.remove(filepath)
            except Exception:
                pass
                
    db.session.delete(expense)
    db.session.commit()
    flash('Expense deleted successfully!', 'success')
    return redirect(url_for('expenses.index'))

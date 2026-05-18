from flask import Blueprint, render_template, request
from flask_login import login_required
from app.models import Expense, Category
from app import db
from datetime import datetime
from sqlalchemy import func, extract

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/')
# @login_required # Commented out until login is fully functional
def index():
    now = datetime.utcnow()
    
    # Read chosen month from query param (Format: "YYYY-MM")
    month_param = request.args.get('month', '')
    
    if month_param:
        try:
            parsed_date = datetime.strptime(month_param, '%Y-%m')
            current_month = parsed_date.month
            current_year = parsed_date.year
        except ValueError:
            current_month = now.month
            current_year = now.year
            month_param = f"{current_year}-{current_month:02d}"
    else:
        current_month = now.month
        current_year = now.year
        month_param = f"{current_year}-{current_month:02d}"
        
    current_month_name = datetime(current_year, current_month, 1).strftime('%B %Y')
    
    # 1. Monthly Total
    monthly_total = db.session.query(func.sum(Expense.amount)).filter(
        extract('month', Expense.expense_date) == current_month,
        extract('year', Expense.expense_date) == current_year
    ).scalar() or 0.0
    
    # Last month total for comparison percentage
    last_month = current_month - 1 if current_month > 1 else 12
    last_month_year = current_year if current_month > 1 else current_year - 1
    last_monthly_total = db.session.query(func.sum(Expense.amount)).filter(
        extract('month', Expense.expense_date) == last_month,
        extract('year', Expense.expense_date) == last_month_year
    ).scalar() or 0.0
    
    percent_change = 0.0
    if last_monthly_total > 0:
        percent_change = ((monthly_total - last_monthly_total) / last_monthly_total) * 100
        
    # 2. Yearly Total
    yearly_total = db.session.query(func.sum(Expense.amount)).filter(
        extract('year', Expense.expense_date) == current_year
    ).scalar() or 0.0
    
    # 3. Budget Remaining
    from flask_login import current_user
    from app.models import User
    if current_user.is_authenticated:
        budget_limit = current_user.yearly_budget
    else:
        admin_user = User.query.filter_by(username='admin').first()
        budget_limit = admin_user.yearly_budget if admin_user else 1000000.0

    budget_remaining = max(0.0, budget_limit - yearly_total)
    
    # 4. Category Breakdown
    categories = Category.query.all()
    # If no categories, seed them
    if not categories:
        default_cats = ['Electricity', 'Salaries', 'Transport', 'Stationery', 'Internet', 'Water Bills', 'Maintenance', 'Furniture', 'Events', 'Miscellaneous']
        for cat_name in default_cats:
            db.session.add(Category(name=cat_name))
        db.session.commit()
        categories = Category.query.all()

    category_data = []
    max_cat_amount = 0
    
    for cat in categories:
        cat_sum = db.session.query(func.sum(Expense.amount)).filter(
            Expense.category_id == cat.id,
            extract('month', Expense.expense_date) == current_month,
            extract('year', Expense.expense_date) == current_year
        ).scalar() or 0.0
        
        if cat_sum > max_cat_amount:
            max_cat_amount = cat_sum
        category_data.append({
            'name': cat.name,
            'amount': cat_sum
        })
        
    # Sort categories by spending descending
    category_data = sorted(category_data, key=lambda x: x['amount'], reverse=True)[:4]
    
    # Calculate relative percentage for progress bar widths
    for item in category_data:
        if max_cat_amount > 0:
            item['percentage'] = (item['amount'] / max_cat_amount) * 100
        else:
            item['percentage'] = 0
            
    # 5. Recent Transactions
    recent_transactions = Expense.query.filter(
        extract('month', Expense.expense_date) == current_month,
        extract('year', Expense.expense_date) == current_year
    ).order_by(Expense.expense_date.desc()).limit(4).all()
    
    return render_template(
        'dashboard/index.html',
        monthly_total=monthly_total,
        percent_change=percent_change,
        yearly_total=yearly_total,
        budget_remaining=budget_remaining,
        category_data=category_data,
        recent_transactions=recent_transactions,
        current_month_name=current_month_name,
        current_month_val=month_param
    )


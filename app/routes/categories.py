from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import Category
from app import db

categories_bp = Blueprint('categories', __name__)

@categories_bp.route('/')
def index():
    categories = Category.query.all()
    # If no categories, seed the default ones
    if not categories:
        default_cats = ['Electricity', 'Salaries', 'Transport', 'Stationery', 'Internet', 'Water Bills', 'Maintenance', 'Furniture', 'Events', 'Miscellaneous']
        for cat_name in default_cats:
            db.session.add(Category(name=cat_name))
        db.session.commit()
        categories = Category.query.all()
        
    return render_template('categories/index.html', categories=categories)

@categories_bp.route('/add', methods=['POST'])
def add():
    name = request.form.get('name')
    if name:
        existing = Category.query.filter_by(name=name).first()
        if existing:
            flash('Category already exists!', 'error')
        else:
            cat = Category(name=name)
            db.session.add(cat)
            db.session.commit()
            flash('Category added successfully!', 'success')
    return redirect(url_for('categories.index'))

@categories_bp.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    cat = Category.query.get_or_404(id)
    if cat.expenses:
        flash('Cannot delete category with associated expenses!', 'error')
    else:
        db.session.delete(cat)
        db.session.commit()
        flash('Category deleted successfully!', 'success')
    return redirect(url_for('categories.index'))

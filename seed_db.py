from app import create_app, db
from app.models import User, Category, Expense
from datetime import datetime, timedelta
import random

app = create_app()

def seed_database():
    with app.app_context():
        # Ensure categories exist
        default_cats = ['Electricity', 'Salaries', 'Transport', 'Stationery', 'Internet', 'Water Bills', 'Maintenance', 'Furniture', 'Events', 'Miscellaneous']
        categories = {}
        for cat_name in default_cats:
            cat = Category.query.filter_by(name=cat_name).first()
            if not cat:
                cat = Category(name=cat_name)
                db.session.add(cat)
                db.session.commit()
            categories[cat_name] = cat.id
            
        # Ensure admin user exists
        admin = User.query.filter_by(username='admin').first()
        if not admin:
            from werkzeug.security import generate_password_hash
            admin = User(username='admin', password_hash=generate_password_hash('password123'), role='Admin', yearly_budget=5000000.0)
            db.session.add(admin)
            db.session.commit()
            
        # Create some realistic expenses for the last 3 months
        print("Seeding expenses...")
        payment_methods = ['Cash', 'Card', 'Bank Transfer', 'UPI']
        
        # Check if expenses already exist to avoid duplicating too many
        if Expense.query.count() < 20:
            for i in range(40):
                # Random date within last 90 days
                days_ago = random.randint(0, 90)
                expense_date = datetime.utcnow().date() - timedelta(days=days_ago)
                
                cat_name = random.choice(default_cats)
                
                # Assign realistic amounts based on category
                if cat_name == 'Salaries':
                    amount = random.uniform(50000, 200000)
                    title = f"Staff Salary - {expense_date.strftime('%B')}"
                elif cat_name == 'Electricity':
                    amount = random.uniform(5000, 25000)
                    title = f"Power Grid Bill - {expense_date.strftime('%B')}"
                elif cat_name == 'Transport':
                    amount = random.uniform(2000, 15000)
                    title = "School Bus Maintenance & Fuel"
                elif cat_name == 'Furniture':
                    amount = random.uniform(10000, 50000)
                    title = "New Classroom Desks"
                else:
                    amount = random.uniform(500, 10000)
                    title = f"{cat_name} Purchase"
                    
                expense = Expense(
                    title=title,
                    description=f"Automated seed entry for {cat_name}.",
                    amount=round(amount, 2),
                    category_id=categories[cat_name],
                    payment_method=random.choice(payment_methods),
                    expense_date=expense_date,
                    created_by=admin.id
                )
                db.session.add(expense)
                
            db.session.commit()
            print("Database successfully seeded with realistic data!")
        else:
            print("Database already has data. Skipping seed.")

if __name__ == '__main__':
    seed_database()

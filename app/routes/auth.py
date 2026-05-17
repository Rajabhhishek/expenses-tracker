from flask import Blueprint, render_template, redirect, flash, request
from flask_login import login_user, logout_user, current_user

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/') 
    
    if request.method == 'POST':
        # Bypass real authentication for now, just go to dashboard
        return redirect('/dashboard')

    return render_template('auth/login.html')

@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect('/auth/login')

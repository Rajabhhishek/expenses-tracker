from flask import Blueprint, render_template, redirect, flash, request, url_for, session
from flask_login import login_user, logout_user, current_user, login_required
import random
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            flash('Logged in successfully.', 'success')
            return redirect(url_for('dashboard.index'))
        flash('Invalid credentials.', 'danger')
    return render_template('auth/login.html')

@auth_bp.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    if request.method == 'POST':
        action = request.form.get('action')
        
        if action == 'update_username':
            new_username = request.form.get('new_username')
            if not new_username:
                flash('Username cannot be empty.', 'danger')
            else:
                existing_user = User.query.filter_by(username=new_username).first()
                if existing_user and existing_user.id != current_user.id:
                    flash('Username already taken.', 'danger')
                else:
                    current_user.username = new_username
                    db.session.commit()
                    flash('Username updated successfully.', 'success')
            return redirect(url_for('auth.settings'))
            
        elif action == 'update_password':
            current_pw = request.form.get('current_password')
            new_pw = request.form.get('new_password')
            confirm_pw = request.form.get('confirm_password')
            
            if not check_password_hash(current_user.password_hash, current_pw):
                flash('Current password is incorrect.', 'danger')
                return redirect(url_for('auth.settings'))
            if new_pw != confirm_pw:
                flash('New passwords do not match.', 'danger')
                return redirect(url_for('auth.settings'))
            if len(new_pw) < 6:
                flash('Password must be at least 6 characters long.', 'danger')
                return redirect(url_for('auth.settings'))
            
            current_user.password_hash = generate_password_hash(new_pw)
            db.session.commit()
            flash('Password updated successfully.', 'success')
            return redirect(url_for('auth.settings'))
        elif action == 'update_budget':
            new_budget = request.form.get('new_budget')
            try:
                new_budget = float(new_budget)
                if new_budget < 0:
                    raise ValueError
                current_user.yearly_budget = new_budget
                db.session.commit()
                flash('Budget updated successfully.', 'success')
            except ValueError:
                flash('Invalid budget amount.', 'danger')
            return redirect(url_for('auth.settings'))
            
    return render_template('auth/settings.html')

@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth_bp.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        username = request.form.get('username')
        user = User.query.filter_by(username=username).first()
        if user:
            # Generate a 6-digit OTP
            otp = str(random.randint(100000, 999999))
            session['reset_username'] = username
            session['otp'] = otp
            # For testing, we just flash the OTP so the user can see it
            flash(f'Your OTP is: {otp}', 'info')
            return redirect(url_for('auth.verify_otp'))
        else:
            flash('Username not found.', 'danger')
    return render_template('auth/forgot_password.html')

@auth_bp.route('/verify_otp', methods=['GET', 'POST'])
def verify_otp():
    if 'reset_username' not in session or 'otp' not in session:
        flash('Session expired or invalid. Please try again.', 'danger')
        return redirect(url_for('auth.forgot_password'))
        
    if request.method == 'POST':
        entered_otp = request.form.get('otp')
        if entered_otp == session.get('otp'):
            session['otp_verified'] = True
            flash('OTP verified successfully.', 'success')
            return redirect(url_for('auth.reset_password'))
        else:
            flash('Invalid OTP. Please try again.', 'danger')
            
    return render_template('auth/verify_otp.html')

@auth_bp.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
    if not session.get('otp_verified') or 'reset_username' not in session:
        flash('Unauthorized access. Please verify OTP first.', 'danger')
        return redirect(url_for('auth.forgot_password'))
        
    if request.method == 'POST':
        new_password = request.form.get('new_password')
        confirm_password = request.form.get('confirm_password')
        
        if new_password != confirm_password:
            flash('Passwords do not match.', 'danger')
        elif len(new_password) < 6:
            flash('Password must be at least 6 characters long.', 'danger')
        else:
            username = session.get('reset_username')
            user = User.query.filter_by(username=username).first()
            if user:
                user.password_hash = generate_password_hash(new_password)
                db.session.commit()
                flash('Password reset successfully. You can now login.', 'success')
                # Clear session
                session.pop('reset_username', None)
                session.pop('otp', None)
                session.pop('otp_verified', None)
                return redirect(url_for('auth.login'))
            else:
                flash('User not found.', 'danger')
                
    return render_template('auth/reset_password.html')

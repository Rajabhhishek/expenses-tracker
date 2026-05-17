from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message_category = 'info'

    with app.app_context():
        from . import models

        from .routes.auth import auth_bp
        app.register_blueprint(auth_bp, url_prefix='/auth')

        from .routes.dashboard import dashboard_bp
        app.register_blueprint(dashboard_bp, url_prefix='/dashboard')

        @app.route('/')
        def index():
            from flask import redirect
            return redirect('/dashboard')

        db.create_all()

    return app

@login_manager.user_loader
def load_user(user_id):
    from .models import User
    return User.query.get(int(user_id))

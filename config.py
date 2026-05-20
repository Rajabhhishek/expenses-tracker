import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Manually load .env file if it exists to avoid external dependencies
if os.path.exists(os.path.join(BASE_DIR, '.env')):
    with open(os.path.join(BASE_DIR, '.env'), 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, val = line.split('=', 1)
                os.environ[key.strip()] = val.strip()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'wisdom-school-default-dev-key')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'wisdom_school.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


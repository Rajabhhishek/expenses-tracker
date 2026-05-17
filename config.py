import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'wisdom-school-secret-key-change-in-prod'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'wisdom_school.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

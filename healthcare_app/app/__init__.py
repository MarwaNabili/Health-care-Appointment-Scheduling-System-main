from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    # Update the URI to use MySQL
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://healthcare_user:your_password@localhost/healthcare'
    app.config['SECRET_KEY'] = 'your_secret_key'

    db.init_app(app)

    # Automatically create database tables
    with app.app_context():
        db.create_all()

    # Import and register your application's routes
    from .routes import main
    app.register_blueprint(main)

    return app

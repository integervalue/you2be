import sqlite3
from flask import current_app, g
from app import app

#Connect to the DB
def get_db():
    with app.app_context():
        DATABASE = current_app.config['DB_PATH']
        db = getattr(g, 'database', None)
        if db is None:
            db = g._database = sqlite3.connect(DATABASE)
        return db
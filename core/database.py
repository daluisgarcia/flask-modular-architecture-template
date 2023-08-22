import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db: SQLAlchemy | None = None


def initialize_db(app: Flask) -> SQLAlchemy:
    """Initialize the database connection"""
    if not app.config.get('DATABASE_ENGINE') or not app.config.get('DATABASE_NAME'):
        raise Exception('Database engine and database name must be set in the config file')

    if app.config.get('DATABASE_ENGINE') == 'sqlite':
        database_uri = f'sqlite:///{os.path.join(app.instance_path, app.config.get("DATABASE_NAME"))}'
    else:
        database_uri = '%s://%s:%s@%s/%s' % (
            app.config.get('DATABASE_ENGINE'),
            app.config.get('DATABASE_USER'),
            app.config.get('DATABASE_PASSWORD'),
            app.config.get('DATABASE_HOST'),
            app.config.get('DATABASE_NAME'),
        )

    app.config['SQLALCHEMY_DATABASE_URI'] = database_uri

    global db
    db = SQLAlchemy(app)

    return db


def establish_db_connection(app: Flask):
    """Creates the database connection and insert the default permissions"""
    with app.app_context():
        db.create_all()

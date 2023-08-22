from flask import Flask
from flask import current_app

from .server import create_app
from .config import config


class AppModule:
    """
    Base class for all modules.

    The **parameters** name and **url_prefix** must be defined in the child class and passed to the constructor.

    The attributes **blueprint**, **permissions_names** and **template_folder** must be defined in the child class with *self*.
    """
    blueprint = None
    permission_names = None
    template_folder = None

    def __init__(self, name: str):
        if not name:
            raise ValueError('MODULE INSTANTIATION ERROR: name must be defined')
        self.name = name

        if not self.blueprint or self.permission_names is None or not self.template_folder:
            raise AttributeError('MODULE INSTANTIATION ERROR: blueprint, template_folder and permissions_names must be defined before calling the AppModule super() constructor')

    def subscribe_templates(self, folder_list: list[str]) -> list[str]:
        """Subscribe the templates folder to the app"""
        if not self.template_folder:
            raise ValueError('Templates folder not defined')

        folder_list.append(self.template_folder)
        return folder_list

    def subscribe_blueprints(self, app: Flask):
        """Subscribe the blueprint to the app"""
        if not self.blueprint:
            raise ValueError('Blueprint not defined')

        app.register_blueprint(self.blueprint)

    def insert_permissions(self, app: Flask):
        """Insert the permissions in the database"""
        if not self.permission_names or len(self.permission_names) == 0:
            return

        from .auth.models import Permission
        with app.app_context():
            db = current_app.config.get('DATABASE_CONNECTION')

            for perm_name in self.permission_names:
                permission = Permission.query.filter_by(name=perm_name).first()
                if not permission:
                    permission = Permission(name=perm_name)
                    db.session.add(permission)
                    db.session.commit()

            db.session.close()


class AppRepository:
    """
    Base class for all repositories.
    """

    def __init__(self):
        self.db = current_app.config.get('DATABASE_CONNECTION')

    def commit(self, record):
        """Commit the record to the database"""
        if not self.db:
            if current_app.config.get('APP_LIFTED'):
                raise ConnectionError('ERROR: No database connection')
            return

        self.db.session.add(record)
        self.db.session.commit()

    def rollback(self):
        """Rollback the database session"""
        self.db.session.rollback()

    def close_session(self):
        """Close the database session"""
        if not self.db:
            if current_app.config.get('APP_LIFTED'):
                raise ConnectionError('ERROR: No database connection')
            return

        self.db.session.close()

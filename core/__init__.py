from flask import Flask
from flask import current_app


from .server import create_app
from .config import config


class AppModule:
    """
    Base class for all modules.

    The **parameters** name and **url_prefix** must be defined in the child class and passed to the constructor.

    The attributes **blueprint**, **models** and **template_folder** must be defined in the child class with *self*.
    """

    def __init__(self, name: str):
        if not name:
            raise Exception('MODULE INSTANTIATION ERROR: name must be defined')
        self.name = name
        self.blueprint = None
        self.template_folder = None

    def subscribe_templates(self, folder_list: list[str]) -> list[str]:
        """Subscribe the templates folder to the app"""
        if not self.template_folder:
            raise Exception('Templates folder not defined')

        folder_list.append(self.template_folder)
        return folder_list

    def subscribe_blueprints(self, app: Flask):
        """Subscribe the blueprint to the app"""
        if not self.blueprint:
            raise Exception('Blueprint not defined')

        app.register_blueprint(self.blueprint)


class AppRepository:
    """
    Base class for all repositories.
    """
    permission_names: list = []

    def __init__(self):
        self.db = current_app.config.get('DATABASE_CONNECTION')

    def commit(self, record):
        """Commit the record to the database"""
        if not self.db:
            if current_app.config.get('APP_LIFTED'):
                raise Exception('ERROR: No database connection')
            return

        self.db.session.add(record)
        self.db.session.commit()

    def close_session(self):
        """Close the database session"""
        if not self.db:
            if current_app.config.get('APP_LIFTED'):
                raise Exception('ERROR: No database connection')
            return

        self.db.session.close()

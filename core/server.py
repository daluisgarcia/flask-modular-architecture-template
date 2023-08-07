import os

from flask import Flask
import jinja2

from core.config import config
from core.database import initialize_db, establish_db_connection
from core.extensions import install_extensions


def create_app(test_config=None) -> Flask:
    """Creates and configures the app"""
    app = Flask(__name__)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        if not config:
            raise Exception('No environment file found... Please create a .env file in the root directory of the project.')

        app.config.from_mapping(dict(config))
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # STATIC FOLDER
    app.static_url_path = '/static'
    # set the absolute path to the static folder
    app.static_folder = app.root_path + app.static_url_path

    # TEMPLATE LIST
    templates_folders = [
        'core/templates',
    ]

    # Initializing the database
    db_conn = initialize_db(app)

    # IMPORTING MODULES LIST
    from modules import APP_MODULES
    # Adding the auth module to the list
    from core.auth.module import AuthModule
    APP_MODULES.add(AuthModule())
    # Registering modules in the app
    for module in APP_MODULES:
        module.subscribe_blueprints(app)
        templates_folders = module.subscribe_templates(templates_folders)

    establish_db_connection(app)

    app.config['DATABASE_CONNECTION'] = db_conn

    # Setting up the template folders
    my_loader = jinja2.ChoiceLoader([
        app.jinja_loader,
        jinja2.FileSystemLoader(templates_folders),
    ])
    app.jinja_loader = my_loader  # This allows to have a templates folder per module

    # Initializing extensions
    install_extensions(app)

    return app

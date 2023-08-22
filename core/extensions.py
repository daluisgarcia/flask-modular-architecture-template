from flask import Flask


def install_extensions(app: Flask):
    """Install flask extensions in the app"""

    # Flask-Login
    from core.auth import init_login_extension
    init_login_extension(app)

    # Flask-Principal
    from core.permissions import init_permission_extension
    init_permission_extension(app)

    # Flask-Migrate

    # Flask-Security

    # Bcrypt

    # Flask-Mail

    # Flask-Bootstrap

    # Flask-Moment

    # Flask-Babel

    # Flask-Admin

    # Flask-Cache

    # Flask-Restless

    # Flask-Assets

    # Flask-Script

    # Flask-DebugToolbar

    # Flask-Webpack

    # Flask-Themes

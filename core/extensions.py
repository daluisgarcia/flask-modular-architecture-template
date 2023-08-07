from flask import Flask


def install_extensions(app: Flask):
    """Install flask extensions in the app"""

    # Flask-Login
    from core.auth import init_login_extension
    init_login_extension(app)

    # Flask-Principal
    from flask_principal import Principal, identity_loaded, UserNeed, RoleNeed
    Principal(app)

    @identity_loaded.connect_via(app)
    def on_identity_loaded(sender, identity):
        from flask_login import current_user
        # Set the identity user object
        identity.user = current_user

        # Add the UserNeed to the identity
        if hasattr(current_user, 'id'):
            identity.provides.add(UserNeed(current_user.id))

        # Update the identity with the roles that the user provides
        if hasattr(current_user, 'roles'):
            for role in current_user.roles:
                for permission in role.permissions:
                    identity.provides.add(RoleNeed(permission.name))

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

    # Flask-Migrate

    # Flask-DebugToolbar

    # Flask-Webpack

    # Flask-Themes

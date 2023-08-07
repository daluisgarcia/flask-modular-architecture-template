from flask_login import LoginManager

from core.auth.repositories.user_repository import UserRepository


def init_login_extension(app):
    """Initializes the auth module"""
    login_manager = LoginManager()
    login_manager.init_app(app)

    login_manager.login_view = "auth.login"

    @login_manager.user_loader
    def load_user(user_id):
        """Used to reload the user object from the user ID stored in the session"""
        user_repo = UserRepository()
        return user_repo.get_user_by_id(user_id)

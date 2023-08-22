from core import AppModule
from core.auth import controllers


class AuthModule(AppModule):

    def __init__(self):
        self.blueprint = controllers.bp
        self.template_folder = 'core/auth/templates'
        self.permission_names = set()
        super().__init__('auth')

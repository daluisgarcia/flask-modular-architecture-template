from core import AppModule
from core.auth import controllers


class AuthModule(AppModule):

    def __init__(self):
        super().__init__('auth')
        self.blueprint = controllers.bp
        self.template_folder = 'core/auth/templates'


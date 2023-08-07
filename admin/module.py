from core import AppModule
from admin import controllers


class AdminModule(AppModule):

    def __init__(self):
        super().__init__('admin')
        self.blueprint = controllers.bp
        self.template_folder = 'admin/templates'

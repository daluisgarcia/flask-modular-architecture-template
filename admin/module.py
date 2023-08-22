from core import AppModule
from admin import controllers
from admin.permissions import EnterAdminPanelPermission


class AdminModule(AppModule):

    def __init__(self):
        self.blueprint = controllers.bp
        self.permission_names = set()
        self.permission_names = self.permission_names.union(EnterAdminPanelPermission().permissions_set)
        self.template_folder = 'admin/templates'
        super().__init__('admin')

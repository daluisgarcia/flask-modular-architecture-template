from core.permissions import AppPermission


class EnterAdminPanelPermission(AppPermission):
    def __init__(self):
        self.permissions_set = {'enter_admin_panel'}
        super().__init__()

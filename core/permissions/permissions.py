from core.permissions import AppPermission


class ManageRolesPermission(AppPermission):
    def __init__(self):
        self.permissions_set = {'manage_user_roles'}
        super().__init__()

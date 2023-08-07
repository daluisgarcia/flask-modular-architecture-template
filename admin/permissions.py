from flask_principal import Permission, RoleNeed


class ManageRolesPermission(Permission):
    def __init__(self):
        need = RoleNeed('manage_user_roles')
        super(ManageRolesPermission, self).__init__(need)

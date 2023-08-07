from core import AppRepository
from core.auth.models import Permission, Role, User


class RolesAndPermissionsRepository(AppRepository):
    permission_names: list = ['manage_user_roles', 'enter_admin_panel']

    def insert_role(self, name: str, permissions: list):
        role = Role(name=name)

        for permission_id in permissions:
            permission = Permission.query.filter_by(id=permission_id).first()
            role.permissions.append(permission)

        self.commit(role)
        self.close_session()

    def bind_user_with_roles(self, user: int, roles: list):
        # Deleting all roles from user
        user = User.query.filter_by(id=user).first()
        user.roles = []
        self.commit(user)

        # Binding user with roles
        for role_id in roles:
            role = Role.query.filter_by(id=role_id).first()
            user.roles.append(role)

        self.commit(user)
        self.close_session()

    def insert_default_permissions(self):
        for perm_name in self.permission_names:
            permission = Permission.query.filter_by(name=perm_name).first()
            if not permission:
                permission = Permission(name=perm_name)
                self.commit(permission)

        permissions = Permission.query.all()
        role = Role.query.filter_by(name='admin').first()
        if not role:
            role = Role(name='admin')
        for permission in permissions:
            role.permissions.append(permission)

        self.commit(role)
        self.close_session()

    @staticmethod
    def get_permissions_choices() -> list:
        permissions = Permission.query.all()
        return [(permission.id, permission.name) for permission in permissions]

    @staticmethod
    def get_roles_created() -> list:
        roles = Role.query.all()
        return [(role.id, role.name) for role in roles]

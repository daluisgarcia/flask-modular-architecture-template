from core import AppRepository
from core.auth.models import Permission, Role, User


class RolesAndPermissionsRepository(AppRepository):

    def __init__(self, permission_names: set = None):
        super().__init__()

        if not permission_names:
            permission_names = set()

        self.permission_names = permission_names

    def insert_role(self, name: str, permissions: list):
        role = Role.query.filter_by(name=name).first()

        if role:
            raise ValueError('Role already exists')

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

    def insert_admin_role_with_permissions(self, permissions_set: set):
        """
        Insert the default roles and permissions
        :return:
        """
        for perm_name in permissions_set:
            try:
                permission = Permission(name=perm_name)
                self.commit(permission)
            except:
                self.rollback()

        role = Role.query.filter_by(name='Admin').first()
        if not role:
            role = Role(name='Admin')

        role.permissions = Permission.query.all()

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

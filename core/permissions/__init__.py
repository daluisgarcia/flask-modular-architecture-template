from flask import Flask
from flask_login import current_user
from flask_principal import Principal, identity_loaded, UserNeed, ActionNeed, Permission


def insert_default_permissions_and_roles(app: Flask):
    """
    Insert the default roles and permissions
    :param app:
    :return:
    """
    with app.app_context():
        from core.permissions.repositories import RolesAndPermissionsRepository
        from core.permissions.permissions import ManageRolesPermission
        RolesAndPermissionsRepository().insert_admin_role_with_permissions(ManageRolesPermission().permissions_set)


class AppPermission(Permission):
    """
    Base class for all permissions definitions

    The **permissions_set** attribute must be defined in the child class *__init__* method.
    """
    permissions_set: set = set()

    def __init__(self, *args, **kwargs):
        # This code for many RoleNeeds in one Permission
        if type(self.permissions_set) is not set:
            raise TypeError('permissions_set attribute must be a set')

        needs = set()
        for permission_name in self.permissions_set:
            needs.add(ActionNeed(permission_name))
        super(AppPermission, self).__init__(*needs)


def init_permission_extension(app: Flask):
    """
    Initialize the Flask-Principal extension
    :param app: Flask application instance
    :return:
    """
    Principal(app)

    # Define the role and permission validation function
    @identity_loaded.connect_via(app)
    def on_identity_loaded(sender, identity):
        # Set the identity user object
        identity.user = current_user

        # Add the UserNeed to the identity
        if hasattr(current_user, 'id'):
            identity.provides.add(UserNeed(current_user.id))

        # Update the identity with the roles that the user provides
        if hasattr(current_user, 'roles'):
            for role in current_user.roles:
                for permission in role.permissions:
                    identity.provides.add(ActionNeed(permission.name))

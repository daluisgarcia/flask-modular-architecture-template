from sqlalchemy import exc
from flask import (
    Blueprint, flash, redirect, render_template, url_for
)
from flask_login import login_required

from core.permissions.permissions import EnterAdminPanelPermission
from core.auth.repositories.user_repository import UserRepository
from core.permissions.forms import BindRolesWithUserForm, CreateRolesForm
from core.auth.repositories.roles_perms_repository import RolesAndPermissionsRepository
from admin.permissions import ManageRolesPermission


bp = Blueprint('admin', __name__, url_prefix='/admin')

manage_role_permission = ManageRolesPermission()
enter_admin_panel_permission = EnterAdminPanelPermission()


@bp.route('/')
@login_required
@enter_admin_panel_permission.require(http_exception=403)
def admin_panel():
    return render_template('dashboard.html')


@bp.route('/roles', methods=('GET', 'POST'))
@login_required
@manage_role_permission.require(http_exception=403)
def create_role():

    form = CreateRolesForm()
    form.permissions.choices = RolesAndPermissionsRepository.get_permissions_choices()


    if form.validate_on_submit():
        try:
            role_perm_repo = RolesAndPermissionsRepository()
            name: str = form.name.data
            permissions: list = form.permissions.data
            role_perm_repo.insert_role(name, permissions)
        except exc.IntegrityError:
            flash(f"Unexpected error.")
        else:
            return redirect(url_for("admin.bind_roles_with_user"))

    return render_template('create_role.html', form=form)


@bp.route('/user/roles', methods=('GET', 'POST'))
@login_required
@manage_role_permission.require(http_exception=403)
def bind_roles_with_user():

    form = BindRolesWithUserForm()
    # This should be done here because the choices dont update if done in the form class
    form.user.choices = UserRepository().get_all_users_for_form()
    form.roles.choices = RolesAndPermissionsRepository.get_roles_created()

    if form.validate_on_submit():
        try:
            role_perm_repo = RolesAndPermissionsRepository()
            user: int = form.user.data
            roles: list = form.roles.data
            role_perm_repo.bind_user_with_roles(user, roles)
        except exc.IntegrityError:
            flash(f"Unexpected error.")
        else:
            return redirect(url_for("blog.index"))

    return render_template('bind_roles_with_user.html', form=form)

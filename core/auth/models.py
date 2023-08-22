from flask_login import UserMixin

from core.database import db


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username: str = db.Column(db.String(50), unique=True, nullable=False)
    password: str = db.Column(db.Text, nullable=False)

    # Relationships
    roles = db.relationship('Role', secondary='user_role')

    def __init__(self, username: str = None, password: str = None):
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User {self.username!r}>'


class PermissionRole(db.Model):
    __tablename__ = 'permission_role'
    permission_id = db.Column(db.Integer(), db.ForeignKey('permission.id', ondelete='CASCADE'), primary_key=True)
    role_id = db.Column(db.Integer(), db.ForeignKey('role.id', ondelete='CASCADE'), primary_key=True)


# Define the Role data-model
class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))

    # Relationships
    permissions = db.relationship('Permission', secondary=PermissionRole.__tablename__, back_populates='roles')


# Define the UserRoles association table
class UserRole(db.Model):
    __tablename__ = 'user_role'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer(), db.ForeignKey('role.id', ondelete='CASCADE'))


class Permission(db.Model):
    __tablename__ = 'permission'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), unique=True)

    # Relationships
    roles = db.relationship('Role', secondary=PermissionRole.__tablename__, back_populates='permissions')

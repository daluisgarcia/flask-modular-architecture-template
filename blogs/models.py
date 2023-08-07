from datetime import datetime
from core.database import db


class Post(db.Model):
    __tablename__ = 'post'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title: str = db.Column(db.Text, nullable=False)
    body: str = db.Column(db.Text, nullable=False)
    author_id: int = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    author = db.relationship('User',
        backref=db.backref('author', lazy=True)) # backref is a relationship that is automatically created on the other side of the relationship.
    created: datetime = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

    comments = db.relationship('Comment', back_populates='post')

    def __init__(self, title: str = None, body: str = None, author_id: int = None):
        self.title = title
        self.body = body
        self.author_id = author_id

    def __repr__(self):
        return f'<User {self.username!r}>'


class Comment(db.Model):
    __tablename__ = 'comment'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    body: str = db.Column(db.Text, nullable=False)
    post_id: int = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)

    post = db.relationship('Post', back_populates='comments')

    def __init__(self, body: str = None, post_id: int = None):
        self.body = body
        self.post_id = post_id

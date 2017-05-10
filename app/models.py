
from . import db

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager
from . import login_manager
from flask_login import UserMixin


#定义Role 和 User 模型
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), unique = True)
    users = db.relationship('User', backref = 'role', lazy = 'dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name     # %r 就是Str 的repr
    


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique = True, index = True)
    username = db.Column(db.String(64), unique = True, index = True)
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username


    #下面是密码部分
    password_hash = db.Column(db.String(128))


    @property
    def password(self):
        raise AttributeError('password is a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


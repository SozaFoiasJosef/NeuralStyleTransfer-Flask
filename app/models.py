from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from . import login_manager

class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %r>' % self.username
    
    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)

class ContentExamples(db.Model):
    __tablename__ = "content_examples"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True)
    image_url = db.Column(db.String(256), unique=True)
    
    def __init__(self, **kwargs):
        super(ContentExamples, self).__init__(**kwargs)

class StyleExamples(db.Model):
    __tablename__ = "style_examples"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True)
    artist = db.Column(db.String(64), index=True)
    image_url = db.Column(db.String(256), unique=True)
    
    def __init__(self, **kwargs):
        super(StyleExamples, self).__init__(**kwargs)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

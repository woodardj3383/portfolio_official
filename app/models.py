from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

class Guest(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fake_name = db.Column(db.String)
    fake_email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)

    def hash_password(self, original_password):
        self.password = generate_password_hash(original_password)

    def check_password(self, original_password):
        return check_password_hash(self.password, original_password)

    def __repr__(self):
        return f"<Guest: {self.fake_email}>"

@login.user_loader
def login_user(id):
    return Guest.query.get(int(id))

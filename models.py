from flask_security import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin):
    def __init__(self, id, password, active=True):
        self.id = id
        self.password_hash = generate_password_hash(password)
        self.active = active

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


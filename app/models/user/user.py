from unicodedata import name
from app.models.base_model import BaseModel
from app import db
from sqlalchemy import func
from flask_login import UserMixin

class User(UserMixin, BaseModel):
    """Users data."""

    __tablename__="user"
    
    name = db.Column(db.String(1000))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    role_id = db.Column(db.Integer, unique=True, nullable=False)


    @classmethod
    def add_user(cls, name, email, password, role_id):
        """Add a new user detail in the database."""
        

        user_detail = User(name=name, email=email, password=password, role_id=role_id)

        db.session.add(user_detail)
        db.session.commit()
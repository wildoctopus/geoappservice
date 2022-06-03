from datetime import datetime

from app import db


class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column("id", db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get(cls, id):
        return cls.query.filter_by(id=id).first()


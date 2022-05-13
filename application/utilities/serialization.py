from datetime import datetime
from enum import Enum
from uuid import UUID

from flask_sqlalchemy import SQLAlchemy

from application import db

primitive = (int, float, str, bool)


def is_primitive(thing):
    return isinstance(thing, primitive)


def serialize(obj, datetime_format=None):
    if obj is None:
        return None
    if is_primitive(obj):
        return obj
    if isinstance(obj, Enum):
        return obj.value
    if isinstance(obj, datetime):
        return obj.isoformat() if not datetime_format else obj.strftime(datetime_format)
    if isinstance(obj, UUID):
        return str(obj)
    if isinstance(obj, list):
        return [serialize(v, datetime_format=datetime_format) for v in obj]
    if isinstance(obj, dict):
        return {
            k: serialize(v, datetime_format=datetime_format) for k, v in obj.items()
        }
    if isinstance(obj, db.Model):
        return {
            column.key: serialize(getattr(obj, attr), datetime_format=datetime_format)
            for attr, column in obj.__mapper__.c.items()
        }
    if isinstance(obj, WKBElement):
        return {}
    return {
        k: serialize(v, datetime_format=datetime_format)
        for k, v in obj.__dict__.items()
    }

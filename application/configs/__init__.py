from application.configs.db import DbDevelopmentConfig
from application.configs.environ import EnvironConfig
from application.configs.constants import Constant

print(DbDevelopmentConfig.USER_DB_CONNECTION_STRING,)
print(EnvironConfig.APP_ENVIRONMENT)


class Config:
    SQLALCHEMY_DATABASE_URI = DbDevelopmentConfig.USER_DB_CONNECTION_STRING
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = EnvironConfig.FLASK_APP_SECRET
    UPLOAD_PATH = Constant.UPLOAD_FOLDER
    

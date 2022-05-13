from application.configs.db import DbDevelopmentConfig
from application.configs.environ import EnvironConfig

print(DbDevelopmentConfig.USER_DB_CONNECTION_STRING,)
print(EnvironConfig.APP_ENVIRONMENT)


class Config:
    SQLALCHEMY_DATABASE_URI = DbDevelopmentConfig.USER_DB_CONNECTION_STRING
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    

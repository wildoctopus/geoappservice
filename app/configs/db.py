import os

class DbProductionConfig:
    DB_URI = ""
    USER_DB_CONNECTION_STRING = os.environ.get(
        "USER_DB_CONNECTION_STRING", os.environ.get("SQLALCHEMY_DATABASE_URI", DB_URI)
    )


class DbQAConfig:
    DB_URI = ""
    USER_DB_CONNECTION_STRING = os.environ.get(
        "USER_DB_CONNECTION_STRING", os.environ.get("SQLALCHEMY_DATABASE_URI", DB_URI)
    )


class DbDevelopmentConfig:

    # edit DB_URI based on your connection string    
    DB_URI="postgresql://postgres:alya@localhost:5432/postgres"
    

    USER_DB_CONNECTION_STRING = os.environ.get(
        "USER_DB_CONNECTION_STRING", os.environ.get("SQLALCHEMY_DATABASE_URI", DB_URI)
    )

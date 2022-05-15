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
    DB_URI="postgresql://postgres:Qwer12345@localhost:5432/mydatabase"
    

    USER_DB_CONNECTION_STRING = os.environ.get(
        "USER_DB_CONNECTION_STRING", os.environ.get("SQLALCHEMY_DATABASE_URI", DB_URI)
    )

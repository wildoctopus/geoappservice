from flask import g, request, url_for
from app.utilities.flask import APIError, APIFlask
from app.configs import Config
from app.configs.environ import EnvironConfig
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from flask import Flask
from app.configs.constants import Constant
from flask_login import LoginManager



db = SQLAlchemy()



def create_app(test_config=None):
    app = APIFlask(__name__, instance_relative_config=True)

    
    if EnvironConfig.APP_ENVIRONMENT.upper()=="PRODUCTION":
        #Add URLs to CORS
        #CORS(app,origins=[Constant.workspace_prod_url, Constant.prod_website_url])
        pass
    else:
        CORS(app)

    
    # app configuration
    app.config.from_object(Config)

    # initialzie db and migrate
    db.init_app(app)
    Migrate(app, db, compare_type=True)
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from app.models.user.user import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    

    
    
    

    with app.app_context():

        #import modules
        from app.routes.airport import india
        from app.routes.auth import auth
        from app.routes.main import main

        #register blueprints        

        app.register_blueprint(india.india_bp)
        app.register_blueprint(auth.auth)
        app.register_blueprint(main.main)
        
        
        return app

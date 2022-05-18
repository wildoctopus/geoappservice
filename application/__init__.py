from flask import g, request, url_for
from application.utilities.flask import APIError, APIFlask
from application.configs import Config
from application.configs.environ import EnvironConfig
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from flask import Flask
from application.configs.constants import Constant



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
    
    

    with app.app_context():

        #imprt modules
        from application.routes.airport import india

        #register blueprints        

        app.register_blueprint(india.india_bp)
        app.register_blueprint(india.entry_bp)
        
        
        return app

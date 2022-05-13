import os
from jinja2 import Environment, PackageLoader, select_autoescape


class EnvironConfig:
    APP_ENVIRONMENT = os.environ.get("APP_ENVIRONMENT", "DEVELOPMENT")
    FLASK_APP_SECRET = os.environ.get("FLASK_APP_SECRET", "XXX_Secret_Key_XXX")
 
    LOGGER_SERVICE_URL = os.environ.get(
        "LOGGER_SERVICE_URL", 
        #edit based on url specified for logger service"
        "http://0.0.0.0:5004"
    )
    

    #Add template related configurations
    templet_env= Environment(loader=PackageLoader('application', 'templates'),autoescape=select_autoescape(['html', 'xml']))

    #sample_template.html file is kept inside templates folder
    #SAMPLE_TEMPLATE = templet_env.get_template('sample_template.html')
    
    



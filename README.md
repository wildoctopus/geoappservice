# geoappservice
A boilerplate code towards modular approach to Python-FLask-PostGIS project. This project structure can be implemented to handle huge number of files.


## Project/Environment setup
* Project is working on PostgreSQL14, Python3.10, PgAdmin4
* Clone the repo - git clone https://github.com/wildoctopus/geoappservice.git
* Navigate to cloned directory and create virtual env. eg - python -m venv .myenv
* Activate the virtual env -<br> 
      If using Unix/Mac OS - ```source .myenv/bin/activate``` <br>
      If using windows run - ```.myenv\Scripts\activate.bat```
      
* Install required packages using requirements.txt - ```pip install -r requirements.txt```

## Falsk DB Migrate
Run below flask commands to migrate db model to physical databse:
* flask db init
* flask db migrate -m "Some message"
* flask db upgrade

## DB Config
Before running the project, make sure to change the Db URI variables based on your local databse connection strings. 
DB config files can be found at : application/configs/db.py

Edit below line in db.py file: 

        DB_URI="postgresql://postgres:XXX@localhost:5432/postgres"


## Run project
Run below command :

        flask run

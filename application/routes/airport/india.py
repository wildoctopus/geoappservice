from flask import Blueprint, request
from flask import Response
from flask import render_template, flash, redirect, url_for
from application.utilities.validation import required_params,validate_json,allowed_file_type_and_size
from application.models.airport.india import IndianAirports
from application.utilities.flask import APIError, APIResponse, validate
from application.utilities.serialization import serialize
from application.forms.addairport import AddForm
from application.forms.mylocation import AddLocationForm
from application.forms.upload import UploadForm
from werkzeug.utils import secure_filename
from http import HTTPStatus
from application import db
from application.configs.constants import Constant
import os
import csv
import io

india_bp = Blueprint("india_route", __name__, url_prefix="/india" )

#Entry route '/'
entry_bp = Blueprint("entry_route", __name__, url_prefix="" )

@entry_bp.route("/")
def welcome():
    return render_template('index.html', title='Welcome')



@india_bp.route("/nearestap",methods=["GET"])
#@required_params(["loc"])
def get_nearest(long, lat):

    '''
    Logic goes here to fetch nearest airport based on latitude and longitude
    '''
    pass

@india_bp.route('/list')
def list_all_airports():
    '''
    dummy_airports_data = [
        {
            'name': 'Mumbai Airport',
            'longitude': 109.45,
            'latitude': 68.56
        },
        {
            'name': 'Delhi Airport',
            'longitude': 43.45,
            'latitude': 54.56
        }
    ]
    '''

    IndianAirportsObj = IndianAirports.get_all()
    return render_template('listairports.html', title='Airport Details', airports = IndianAirportsObj)


@india_bp.route('/addairport', methods=['GET', 'POST'])
def add_airport():
    form = AddForm()
    if form.validate_on_submit():

        #Check if coordinates already exists in databse
        locationExists = IndianAirports.get_location(form.longitude.data, form.latitude.data)
        if not locationExists:
            IndianAirportsModelObj = IndianAirports.add_airport(form.name.data, form.longitude.data, form.latitude.data)
            flash('Added data for Airport {}'.format(form.name.data))
            return redirect(url_for('india_route.list_all_airports'))
        flash('Details already exists in Database!')
    return render_template('addairport.html', title='Add Airport', form=form)


@india_bp.route('/nearestairport', methods=['GET', 'POST'])
def get_nearest_airport():
    form = AddLocationForm()
    if form.validate_on_submit():
        airport = IndianAirports.get_nearest_loc(form.longitude.data, form.latitude.data)
        flash('Nearest Airport: {} , Long: {}, Lat: {}'.format(airport.name, airport.longitude, airport.latitude))        
        return redirect(url_for('india_route.get_nearest_airport'))
    return render_template('enterloc.html', title='Nearest Airport', form=form)


@india_bp.route('/enterloc', methods=['GET', 'POST'])
def get_location():

    airport = IndianAirports.get_nearest_loc(request.form.longitude, request.form.latitude)
    
    return render_template('nearestairport.html', title='Nearest Airport', airport=airport)

'''
#Dummy route to test nearest location.
@india_bp.route('/result')
def get_loc():

    long = 12.45
    lat = 23.22

    airport = IndianAirports.get_nearest_loc(long, lat)    
    return render_template('nearestairport.html', title='Nearest Airport', airport=airport)
'''


@india_bp.route('/delete/<int:id>', methods=['GET','POST'])
def delete(id):
    IndianAirportsObj = IndianAirports.get_by_id(id = id)
    print("hello")
    #if request.method == 'POST':
    if IndianAirportsObj:
        print("hello")
        db.session.delete(IndianAirportsObj)
        db.session.commit()
        return redirect(url_for('india_route.list_all_airports'))
    flash('Detail not found.')
    return redirect(url_for('india_route.list_all_airports'))
 
    #return redirect(url_for('india_route.list_all_airports'))


@india_bp.route('/deleteall', methods=['GET','POST'])
def delete_all():
    
    try:
        num_rows_deleted = IndianAirports.query.delete()
        db.session.commit()        

    except:
        db.session.rollback()
        
    if num_rows_deleted:
        return redirect(url_for('india_route.list_all_airports'))   
    flash('Details not found.')
 
    return redirect(url_for('india_route.list_all_airports'))
    

@india_bp.route('/upload', methods=['GET','POST'])
def upload():
    form = UploadForm()
    if form.validate_on_submit():
        uploaded_file = form.file.data
        filename = secure_filename(form.file.data.filename)
        file_path = os.path.join(Constant.UPLOAD_FOLDER, filename)
        uploaded_file.save(file_path)
        #filestream.seek(0)
        print(filename)
        processCSV(filename=file_path)

        flash('File uploaded')        
        return redirect(url_for('india_route.list_all_airports'))
 
    return render_template('upload.html', title='File Upload', form=form)


def processCSV(filename):
    with open(filename, 'r') as csv_file:
        reader = csv.reader(csv_file)
        #print(str(reader))

        buffer = []
        for row in reader:
            buffer.append({
                'name': row[0],
                'longitude': float(row[1]),
                'latitude': float(row[2]),
                'geo': 'POINT({} {})'.format(float(row[1]), float(row[2]))
            })
            if len(buffer) % 10000 == 0:
                db.session.bulk_insert_mappings(buffer)
                buffer = []
        print(buffer)

        db.session.bulk_insert_mappings(IndianAirports, buffer)
        db.session.commit()
    
    

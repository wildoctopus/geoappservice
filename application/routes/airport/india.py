from flask import Blueprint, request
from flask import Response
from flask import render_template, flash, redirect, url_for
from application.utilities.validation import required_params,validate_json,allowed_file_type_and_size
from application.models.airport.india import IndianAirports
from application.utilities.flask import APIError, APIResponse, validate
from application.utilities.serialization import serialize
from application.forms.addairport import AddForm
from http import HTTPStatus

india_bp = Blueprint("india_route", __name__, url_prefix="/india" )


@india_bp.route("/nearestap",methods=["GET"])
#@required_params(["loc"])
def get_nearest_airport(long, lat):

    '''
    Logic goes here to fetch nearest airport based on latitude and longitude
    '''
    pass

@india_bp.route('/addairport', methods=['GET', 'POST'])
def add_airport():
    form = AddForm()
    if form.validate_on_submit():
        flash('Added data for Airport {}'.format(form.name.data))
        return redirect(url_for('index'))
    return render_template('addairport.html', title='Add Airport', form=form)
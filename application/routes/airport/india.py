from flask import Blueprint, request
from flask import Response
from application.utilities.validation import required_params,validate_json,allowed_file_type_and_size
from application.models.airport.india import IndianAirports
from application.utilities.flask import APIError, APIResponse, validate
from application.utilities.serialization import serialize
from http import HTTPStatus

india_bp = Blueprint("india_route", __name__, url_prefix="/india" )


@india_bp.route("/nearestap",methods=["GET"])
#@required_params(["loc"])
def get_nearest_airport(long, lat):

    '''
    Logic goes here to fetch nearest airport based on latitude and longitude
    '''
    pass

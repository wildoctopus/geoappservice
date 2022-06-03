from http import HTTPStatus

from flask import request
from cerberus import  Validator
from app.utilities.flask import APIError
import os

def required_params(params):
    def wrapper(func):
        def inner(*args, **kwargs):
            request_param_dict = request.get_json() or request.args
            for param in params:
                if param not in request_param_dict:
                    return APIError(
                        message=f"{param} is required", status=HTTPStatus.BAD_REQUEST
                    )
                kwargs.update({param: request_param_dict[param]})
            return func(*args, **kwargs)

        inner.__name__ = func.__name__
        return inner

    return wrapper


def validate_json(schema):
    def wrapper(func):
        def inner(*args, **kwargs):
            json = request.get_json() 
            validation=Validator(schema)
            validation_result = validation.validate(json)
            if  not validation_result:
                return APIError(message="Validation error",data=validation.errors,status=HTTPStatus.BAD_REQUEST)
            return func(*args, **kwargs)
        inner.__name__ = func.__name__
        return inner

    return wrapper


def allowed_file_type_and_size(file_type,file_size):
    def wrapper(func):
        def inner(*args, **kwargs):
            media_length = request.content_length
            uploaded_file = request.files['media']
            filename = uploaded_file.filename
            file_ext = os.path.splitext(filename)[1]
            if file_ext.lower() not in file_type:
                    return APIError(message="Not a valid File ",status=HTTPStatus.BAD_REQUEST)
            if media_length is not None and media_length > file_size * 1024 * 1024 : 
                    return APIError(message=f"File size is more than {file_size} MB. ",status=HTTPStatus.BAD_REQUEST)
            return func(*args, **kwargs)
        inner.__name__ = func.__name__
        return inner
    return wrapper
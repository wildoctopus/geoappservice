from flask import Blueprint, redirect, render_template, url_for
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/')
def welcome():
    return render_template('index.html', title='Welcome')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', title='Hi', name=current_user.name)

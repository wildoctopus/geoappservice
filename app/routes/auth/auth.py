from flask import Blueprint, render_template, flash, redirect, url_for
from app.forms.login import LoginForm
from app.models.user.user import User
from flask_login import login_required, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        remember_me = True if form.remember_me.data else False
        user = User.query.filter_by(email=form.email.data).first()
        if not user or not check_password_hash(user.password, form.password.data):

            flash('Please check your login details and try again.')
            return redirect(url_for('auth.login'))
            '''
                if form.remember_me.data:
                    login_user(user, remember=True, duration=timedelta(days=5))
                else:
                    login_user(user)
                    # login_user(user, remember=False) 
                flash('Successful Login', 'success')
                next_url = request.args.get('next')
                if not next_url or url_parse(next_url).netloc != '':
                    return redirect(url_for("thankyou"))
                return redirect(next_url)
            else:
                flash('Incorrect Username or Password', 'danger')
                form.username.data = ''
                form.password.data = ''
            '''
        else:
            login_user(user, remember=remember_me)
            return redirect(url_for('main.profile'))

    return render_template("login.html", form=form)

@auth.route('/signup')
def signup():
    return 'Signup'

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.welcome'))


@auth.route('/addtempusers', methods=['GET'])
def add_user():
    adminobj = User.query.filter_by(email='admin@admin.com').first()
    guestobj = User.query.filter_by(email='guest@guest.com').first()

    if adminobj and guestobj:
        flash('Details already exists.')
    else:
        User.add_user('Admin', 'admin@admin.com', generate_password_hash('admin', method='sha256'), 1)
        User.add_user('Guest', 'guest@guest.com', generate_password_hash('guest', method='sha256'), 2)
        flash('Added temp data')
    
    return redirect(url_for('auth.login'))

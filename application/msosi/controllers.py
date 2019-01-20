from flask import render_template, Blueprint, redirect, request, flash, url_for
from flask_login import logout_user, login_user, login_required, LoginManager, current_user

from application import app
from forms.user_login_form import UserLoginForm
from forms.user_reg_form import UserRegForm
from models.user_regisration import UserRegistration

home = Blueprint('msosi', __name__, template_folder='templates',
                 static_folder='static')

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return UserRegistration.objects(pk=user_id).first()


@home.route('/')
def home_page():
    return render_template('home/new_home.html')


@home.route('/register', methods=['GET', 'POST'])
def registration_page():
    """ Enables new user registration."""
    user_data = request.form
    form = UserRegForm(user_data)
    if form.validate_on_submit():
        existing_user = UserRegistration.objects(email=form.email.data).first()
        if existing_user is None:
            form.populate_obj(UserRegistration)
            add_user_to_db = UserRegistration.save()
            login_user(add_user_to_db, remember=True)
            flash('You are now registered and can login in', 'success')
            return redirect(url_for('dashboard'))

    return render_template('home/register.html', form=form)


@home.route('/login', methods=['GET', 'POST'])
def login():
    """ Returns: Returns logged in user to dashboard. """
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    user_data = request.form
    form = UserLoginForm(user_data)
    if form.validate_on_submit():
        check_user = UserRegistration.objects(email=form.email.data).first()
        if check_user:
            if check_user['password'] == form.password.data:
                login_user(check_user)
                return redirect(url_for('dashboard'))
    return render_template('home/login.html')


@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('home/dashboard.html')


@app.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    flash('You were logged out.')
    return redirect(url_for('msosi.home_page'))


@app.route('/user-profile')
@login_required
def user_profile():
    return render_template('home/user_profile.html')


@app.route('/menu')
@login_required
def menu():
    return render_template('home/menu.html')


@app.route('/orders')
@login_required
def orders():
    return render_template('home/orders.html')

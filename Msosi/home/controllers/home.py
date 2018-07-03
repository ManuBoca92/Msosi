from flask import render_template, Blueprint, redirect, request, flash, url_for
from models.user_regisration import UserRegistration
from models.user_login import UserLogin
from flask_login import logout_user, login_user, login_required, login_manager, LoginManager, current_user
from forms.user_login_form import UserLoginForm
from forms.user_reg_form import UserRegForm
from Msosi import app

home = Blueprint('home', __name__, template_folder='templates',
                 static_folder='static')

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return UserRegistration.objects(pk=user_id).first()

@home.route('')
def index():
    return render_template('home/new_home.html')


@home.route('/register', methods=['GET','POST'])
def registration_page():
    user_data = request.form
    form = UserRegForm(user_data)
    if request.method == 'POST':
        existing_user = UserRegistration.objects(email=form.email.data).first()
        if existing_user is None:
            # hashpass = generate_password_hash(form.password.data, method='sha256')
            add_user_to_db = UserRegistration(form.firstName.data, form.lastName.data,
                                              form.address.data, form.city.data,
                                              form.email.data, form.password.data, form.confirm.data).save()
            login_user(add_user_to_db, remember=True)
            flash('You are now registered and can login in', 'success')
            return redirect(url_for('dashboard'))

    return render_template('home/register.html', form=form)

@home.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated == True:
        return  redirect(url_for('dashboard'))
    user_data = request.form
    form = UserLoginForm(user_data)
    if request.method == 'POST':
        check_user = UserRegistration.objects(email=form.email.data).first()
        if check_user:
            if check_user['password'] == form.password.data:
                login_user(check_user)
                return redirect(url_for('dashboard'))
    return render_template('home/login.html')
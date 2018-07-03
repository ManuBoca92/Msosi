from flask import Flask, render_template,redirect, url_for, request, jsonify, flash, session
from flask_mongoengine import MongoEngine
from flask_login import logout_user, login_user, login_required, login_manager, LoginManager, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import os
from flask_cache import Cache
from models.user_regisration import UserRegistration
from models.user_login import UserLogin
from forms.user_reg_form import UserRegForm



app = Flask(__name__)
app.config.from_pyfile('config.py')
app.config['SECRET_KEY'] = '12345679'
db = MongoEngine(app)
cache = Cache(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return UserRegistration.objects(pk=user_id).first()

@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

@app.route('/')
@cache.cached(timeout=60)
def index():
    # return render_template('home.html')
    return render_template('newnew.html')

@app.route('/home')
def redirect_to_homepage():
    return redirect(url_for('index'))

@app.route('/register', methods=['GET','POST'])
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

    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
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
    return render_template('login.html')


@app.route('/forgot-password')
def forgot_password():
    return render_template('forgot_password.html')


@app.route('/dashboard')
@login_required
def dashboard():
    form = UserRegistration()
    name = form.firstName
    print(name)
    user = current_user
    return render_template('dashboard.html')

@app.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    flash('You were logged out.')
    return redirect(url_for('index'))

@app.route('/orders')
def orders():
    mess = flash('You currently have no orders')

    return render_template('orders.html')

if __name__ =='__main__':
    app.run(debug=True)
from flask import Flask, render_template, redirect, request, abort, url_for
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from data.cart_model import CartItem
from data.product_model import Product
from data.user_model import User
from flask_restful import Api
from requests import get, post, delete
from data import db_session
from forms.user_form import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

api = Api(app)

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


def main():
    app.run(port=8080)


@app.route('/')
def index():
    session = db_session.create_session()
    return render_template('index.html', title='Главная')


@app.route('/register', methods=['GET', 'POST'])
def register():
    session = db_session.create_session()
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(name=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        session.add(user)
        session.commit()
        return redirect(url_for('index'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    session = db_session.create_session()
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('index'))
    return render_template('loginform.html', title='Sign In', form=form)


if __name__ == '__main__':
    db_session.global_init("db/store.db")
    main()

from flask import Flask, render_template, redirect, request, abort, url_for
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from data.cart_model import CartItem
from data.product_model import Product
from data.user_model import User
from flask_restful import Api
from requests import get, post, delete
from data import db_session
from forms.user_form import RegistrationForm, LoginForm
from forms.addprod_form import AddProductForm
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
import os
from data.db_methods import Thing

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/store.db'
app.config['UPLOAD_FOLDER'] = 'static/img'
db = SQLAlchemy(app)

api = Api(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    session = db_session.create_session()
    return session.query(User).get(user_id)


def main():
    app.run(debug=True, port=8080)


@app.route('/')
def index():
    products = Thing.get_all()
    return render_template('index.html', title='SWAG DRIP STORE - Главная', products=products)


@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html', title='О НАС')


@app.route('/diligence', methods=['GET', 'POST'])
def diligence():
    return render_template('diligence.html', title='Пособие по уходу')


@app.route('/payment', methods=['GET', 'POST'])
@login_required
def payment():
    return render_template('payment.html', title='Оплата')


@app.route('/register', methods=['GET', 'POST'])
def register():
    session = db_session.create_session()
    form = RegistrationForm()
    if form.validate_on_submit():
        if form.password.data != form.confirm_password.data:
            return render_template('register.html', title='Регистрация', form=form)
        if session.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация', form=form)
        user = User(name=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        session.add(user)
        session.commit()
        return redirect('/')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        session = db_session.create_session()
        user = session.query(User).filter(User.name == form.username.data).first()
        if user is not None and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect('/')
    return render_template('loginform.html', title='Войти', form=form)


@app.route('/add_product', methods=['GET', 'POST'])
@login_required
def add_product():
    session = db_session.create_session()
    form = AddProductForm()
    if form.validate_on_submit():
        image = form.image.data
        if image and image.filename:
            image_filename = secure_filename(image.filename)
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], image_filename)
            image.save(image_path)
            print("Изображение успешно сохранено по пути:", image_path)

            with open(image_path, 'rb') as f:
                image_bytes = f.read()

            product = Product(name=form.name.data, price=form.price.data, quantity=form.quantity.data,
                              seller_id=current_user.id, image=image_bytes)
            session.add(product)
            session.commit()
            return redirect('/')
        else:
            print("Изображение не выбрано")
    return render_template('new_product.html', title='Добавить товар', form=form)


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect('/')


if __name__ == '__main__':
    db_session.global_init("db/store.db")
    main()

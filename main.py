from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    app.run(port=8800)


@app.route('/')
def index():
    return render_template('templates/index.html')


if __name__ == '__main__':
    db_session.global_init("db/store.db")
    main()

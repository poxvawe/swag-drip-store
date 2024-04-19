from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
ref = "https://www.youtube.com/watch?v=hlwlM4a5rxg"


def main():
    app.run(port=8800)


@app.route('/')
def index():
    return render_template('templates/index.html')


if __name__ == '__main__':
    main()

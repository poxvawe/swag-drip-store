from flask import render_template
from main import app


@app.route('/')
def index():
    products = Product.query.all()
    products = []
    return render_template('index.html', products=products)

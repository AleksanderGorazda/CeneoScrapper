from app import app
from flask import render_template
from flaskext.markdown import Markdown
from app.forms import ProductForm
from app.models import Product, Opinion
import requests


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/scrapper')
def scrapper():
    return "Podaj kod produktu do pobrania opinii"

@app.route('/products')
def products():
    pass

@app.route('/about')
def about():
    content = ''
    with open("README.md", 'r', encoding="UTF-8") as f:
        content = f.read()
    return render_template("about.html", tekst=content)

@app.route('/extract', methods = ['POST', 'GET'])
def extract():
    form = ProductForm()
    if form.validate_on_submit():
        page_response = requests.get("https://www.ceneo.pl/"+request.form['product_code'])
        if page_response.status_code == 200:
            product = Product(form.product_code)
            return "OK"
        else:
            form.product_code.errors.append("Dla podanego kodu nie ma produktu")
            return render_template("extract.html", form=form)
        return "Przesłano formularz"
    return render_template("extract.html", form=form)

@app.route('/product/<product_id>')
def product():
    pass

@app.route('/analyzer/<product_id>')
def analyzer():
    return "Podaj kod produktu do analizy"
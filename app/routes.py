from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World"

@app.route('/scraper')
def scrapper():
    return "Podaj kod produktu do pobrania opinii"

@app.route('/analyzer')
def analyzer():
    return "Podaj kod produktu do analizy"
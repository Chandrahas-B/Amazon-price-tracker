from flask import Flask, render_template, request
from .scraper import get_page 
from .models import insert_products
    
app = Flask(__name__)

@app.route('/', methods= ["GET"])
def index():
    return render_template('index.html')
  
@app.route('/results', methods= ["GET", "POST"])
def results():
    if request.method == "POST":
        name = request.form.get("name")
        name = '+'.join(name.split(' '))
        url = "https://www.amazon.in/s?k=" + name
        product_list, urls = get_page(url)
        # print(urls)
        insert_products(product_list)
        return render_template("results.html", url = url, name = name, product_list = product_list, urls = urls)
from flask import Flask, render_template, request, session
from .scraper import get_page, get_image_url
from .models import insert_products, get_product_id, get_product_from_id, get_product_prices
from .helper import get_price_and_time
import asyncio
    
app = Flask(__name__)
app.secret_key = '12345'

@app.template_filter()
def format_currency(value):
    return format(int(value), ',d')


@app.route('/', methods= ["GET"])
def index():
    return render_template('index.html')
  
@app.route('/results', methods= ["GET", "POST"])
def results():
    if request.method == "POST":
        name = request.form.get("name")
        url = "https://www.amazon.in/s?k=" + '+'.join(name.split(' '))
        product_list, urls = get_page(url)
        ids = {}
        session['urls'] = urls
        insert_products(product_list)
        for product in product_list:
            ids[product] = get_product_id(product)
        return render_template("results.html", url = url, name = name, product_list = product_list, urls = urls, ids = ids)
    

@app.route('/details/<name>')
def details(name: str):
    id = request.args.get('id')
    print(id, name)
    product_name = get_product_from_id(int(id))
    url = session['urls'][product_name]
    prices_and_scraped_times = get_product_prices(product_name)
    prices, scraped_times = get_price_and_time(prices_and_scraped_times)
    # image_url = get_image_url(url)
    image_url = None
    return render_template('details.html', id = id, product_name = product_name, 
                        name = name, url = url, prices = prices, scraped_times = scraped_times, image_url = image_url)
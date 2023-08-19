from flask import Flask, render_template, request
from .models import conn


if conn:
    print("Connection sucessful")
else:
    print(conn)
    
    
app = Flask(__name__)

@app.route('/', methods= ["GET"])
def index():
    return render_template('index.html')

@app.route('/results', methods= ["GET", "POST"])
def results():
    # if request.method == "POST":
        pass
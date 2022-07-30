from dotenv import load_dotenv
from flask import Flask, render_template
import os


load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/bronze')
def bronze():
    return render_template('bronze.html')

@app.route('/silver')
def silver():
    return render_template('silver.html')

@app.route('/gold')
def gold():
    return render_template('gold.html')


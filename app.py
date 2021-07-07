import configparser
import os

import requests
from flask import Flask, render_template, request


app = Flask(__name__)

app.config['api_key'] = os.environ.get('API_KEY')
app.config['api_url'] = os.environ.get('API_URL')


@app.route("/")
def intro():
    return render_template('intro.html')


@app.route("/home")
def home():
    return render_template('home.html', api_key=api_key)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/features")
def features():
    return render_template('features.html', title='Features')


def get_weather_results(zip_code, api_key):
    r = requests.get(api_url.format(zip_code, api_key))
    return r.json()


@app.route('/results', methods=['POST'])
def render_results():
    zip_code = request.form['zipCode']

    api_key = '520b4b238162918bbe357f916e8b21ee'
    data = get_weather_results(zip_code, api_key)
    temp = "{0:.1f}".format(data["main"]["temp"])
    feels_like = "{0:.1f}".format(data["main"]["feels_like"])
    weather = data["weather"][0]["main"]
    location = data["name"]

    return render_template('home.html',
                           location=location, temp=temp,
                           feels_like=feels_like, weather=weather)





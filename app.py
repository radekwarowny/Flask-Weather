import configparser
import os

import requests
from flask import Flask, render_template, request


app = Flask(__name__)

app.config['API_KEY'] = os.environ.get('API_KEY')

geo_url = "https://ip-geolocation.whoisxmlapi.com/api/v1?apiKey=at_c6uADJia87Lvd538rTySm1bQFqyNG&ipAddress=8.8.8.8"

API_KEY = '520b4b238162918bbe357f916e8b21ee'


@app.route("/")
def intro():
    return render_template('intro.html')


@app.route("/home")
def home():
    return render_template('home.html', API_KEY=API_KEY)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/features")
def features():
    return render_template('features.html', title='Features')


def get_weather_results(zip_code, api_key):
    api_url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}".format(zip_code, api_key)
    r = requests.get(api_url)
    return r.json()


@app.route('/results', methods=['POST'])
def render_results():

    geo = requests.get(geo_url)
    result = geo.json()

    radek = result["location"]["city"]
    zip_code = request.form['zipCode']

    api_key = '520b4b238162918bbe357f916e8b21ee'
    data = get_weather_results(zip_code, api_key)
    temp = "{0:.1f}".format(data["main"]["temp"])
    feels_like = "{0:.1f}".format(data["main"]["feels_like"])
    weather = data["weather"][0]["main"]
    location = data["name"]

    return render_template('home.html',
                           location=location, temp=temp,
                           feels_like=feels_like, weather=weather, radek=radek)





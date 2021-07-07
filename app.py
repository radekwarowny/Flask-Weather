import os
import requests
from flask import Flask, render_template, request


app = Flask(__name__)

app.config['API_KEY'] = os.environ.get('API_KEY')
app.config['API_URL'] = os.environ.get('API_URL')
print(app.config['API_KEY'])


@app.route("/")
def intro():
    return render_template('intro.html')


@app.route("/home")
def home():
    key = app.config['API_KEY']
    return render_template('home.html', key=key)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/features")
def features():
    return render_template('features.html', title='Features')


def get_weather_results(zip_code, api_key):
    url = app.config['API_URL']
    r = requests.get(url.format(zip_code, api_key))
    print(url)
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





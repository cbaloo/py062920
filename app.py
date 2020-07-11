
import requests
import sqlite3
from sqlite3 import Error
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['DEBUG'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'#'sqlite:///C:\\Users\\chand\\weather_app\\weather.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

@app.route('/')
def index_get():
    
    cities = City.query.all()

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=17ff142c43dfd10e353ad96ce288a49d'
    

    weather_data = []

    for city in cities:

        r = requests.get(url.format(city.name)).json()

        weather = {
            'city' : city.name,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }

        weather_data.append(weather)


    return render_template('weather.html', weather_data=weather_data) 



    @app.route('/', methods=['POST'])
    def index_post():
    
        new_city = request.form.get('city')

        if new_city:
            new_city_obj = City(name=new_city)

            db.session.add(new_city_obj)
            db.session.commit()

    return redirect(url_for('index_get'))

   # if __name__ == '__main__':
    #    app.run()

     
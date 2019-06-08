from flask import Flask, render_template, url_for, request
from static import forecast

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title='Home | ThePyGuy')


@app.route('/display_forecast')
def display_forecast():
    city = request.args.get('city_name')
    data = forecast.weather_data(city)
    title = city.title() + ' | ThePyGuy'
    if type(data) is str:
        return render_template('display_forecast.html', title='ThePyGuy', got=False, data=data)
    else:
        return render_template('display_forecast.html', title=title, got=True, data=data)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run()

from flask import Flask, render_template, request, url_for
from static import forecast

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title='Home | ThePyGuy')


@app.route('/display_forecast')
def display_forecast():
    city = request.args.get('city_name')
    fdata = forecast.forecast(city)
    if type(fdata) is str:
        return render_template('display_forecast.html', got=False, title='No data found')
    return render_template('display_forecast.html', title=fdata[0]+' | ThePyGuy', location=fdata[0],
                           current_data=fdata[1], forecast_data=fdata[2], got=True)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run()

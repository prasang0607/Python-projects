from flask import Flask, render_template, request
from static import get_movie_info

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title='Home | ThePyGuy')


@app.route('/movie_details')
def movie_details():
    name = request.args.get('movie_name')
    info = get_movie_info.movie_info(name)
    title = name.title() + ' | ThePyGuy'
    if type(info) is dict: return render_template('show_info.html', title=title, data=info, got=True)
    else: return render_template('show_info.html', title=title, data=info, got=False)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run()

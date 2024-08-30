from flask import Flask, render_template

from api import get_image_from_api

app = Flask(__name__)


@app.errorhandler(500)
def bad_request_error(error):
    return render_template('500.html'), 500


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.route('/')
def index():
    image_urls = get_image_from_api()
    return render_template('index.html', image_urls=image_urls)


if __name__ == '__main__':
    app.run()

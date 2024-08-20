from flask import Flask, render_template

from api import get_image_from_api

app = Flask(__name__)


@app.route('/')
def index():
    image_urls = get_image_from_api()
    return render_template('index.html', image_urls=image_urls)


if __name__ == '__main__':
    app.run()

from flask import Flask,render_template

from scrapingmodule import random_thoughts


app = Flask(__name__)

@app.route('/')
def mainweb():
    return render_template('index.html', idea=random_thoughts())


if __name__ == "__main__":
    app.run()
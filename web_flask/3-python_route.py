#!/usr/bin/python3

"""script starts a flask web application"""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """return hello HBNB"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns hbnb"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def mytext(text):
    """returns C text"""
    new_text = escape(text).replace('_', ' ')
    return f'C {new_text}'


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=Flase)
def pytext(text):
    """returns python text"""
    new_text = escape(text).replace('_', ' ')
    return f'python {new_text}'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')

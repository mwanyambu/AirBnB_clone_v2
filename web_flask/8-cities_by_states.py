#!/usr/bin/python3

"""start falsk web app"""

from flask import Flask, render_template
from models import storage
from models import *

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """remove current session"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def state_cities():
    """displays states with their cities"""
    states = storage.all(State).values()
    return render_template('cities_by_states.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')

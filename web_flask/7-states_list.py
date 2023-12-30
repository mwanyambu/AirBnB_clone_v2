#!/usr/bin/python3

"""script that starts flask"""

from flask import Flask, render_template
from models import storage
from models import *
from os import environ as env

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """removes current session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """display a html page with states list"""
    states = storage.all(State).values()
    assorted = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=assorted)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')

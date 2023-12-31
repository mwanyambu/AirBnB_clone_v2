#!/usr/bin/python3

"""start flask web application"""

from flask import Flask, render_template
from models import *
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """stops current session"""
    storage.close()


@app.route('/states', strict_slashes=False)
def state():
    """displays states html"""
    states = storage.all(State)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states(id):
    """shows states"""
    for state in storage.all(State).values():
        if state.id == id:
            return render_template('9-states.html', state=state)
    return render_template('9-states.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')

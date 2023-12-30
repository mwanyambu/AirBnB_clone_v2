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
@app.route('/states/<id>', strict_slashes=False)
def states(state_id=None):
    """shows states"""
    states = storage.all("State")
    if state_id is not None:
        state_id = 'Stae.' + state_id
    return render_template('9-states.html', states=states state_id=state_id)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')

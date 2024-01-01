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


"""@app.route('/states', strict_slashes=False)
def state():
    displays states html
    states = storage.all(State)
    return render_template('9-states.html', states=states)"""


@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def city_states(state_id=None):
    """displays states and their cities"""
    states = storage.all("State").values()
    if state_id:
        state_key = "State.{}".format(state_id)
        state = storage.get(State, state_key)
        if state:
            cities = sorted(state.cities, key=lambda city: city.name)
            return render_template('9-states.html', state=state, cities=cities)
        return render_template('9-states.html', not_found=True)
    return render_template('9-states.html', states=sorted(states,
                           key=lambda state: state.name))


"""@app.route('/states/<id>', strict_slashes=False)
def states(id):
    shows states
    for state in storage.all(State).values():
        if state.id == id:
            return render_template('9-states.html', state=state)
    return render_template('9-states.html')"""


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')

#!/usr/bin/python3
"""
A script that start a flask web application
"""
from flask import Flask, render_template
from models import storage
from os import environ as env

app = Flask(__name__)


@app.teardown_appcontext
def shutdown_session(exception=None):
    """closes the storage session after each request"""
    storage.close()


@app.route("/states/<id>", strict_slashes=False)
@app.route("/states", strict_slashes=False)
def states_cities_list(id=None):
    """
    Description:
        show state and cities if id is given
        otherwise list all states.
    parameter:
        id- The id of state or city in Storage.
    """
    states = storage.all("State")
    if id:
        state = states.get('State.{}'.format(id))
        states = [state] if state else []
    else:
        states = list(states.values())
    states.sort(key=lambda x: x.name)
    for state in states:
        state.cities.sort(key=lambda x: x.name)
    return render_template(
        '9-states.html',
        states=states,
        len=len(states),
        id=id
    )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

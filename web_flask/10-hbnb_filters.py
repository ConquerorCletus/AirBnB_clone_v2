#!/usr/bin/python3
"""
A script that start a flask web application
"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def shutdown_session(exception=None):
    """closes the storage session after each request"""
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def states_cities_list():
    """
    Description:
    show state and cities if id is given
    otherwise list all states.
    parameter:
        id:The id of state or city in Storage.
    """
    states = list(storage.all("State").values())
    states.sort(key=lambda x: x.name)
    for state in states:
        state.cities.sort(key=lambda x: x.name)
    amenities = list(storage.all("Amenity").values())
    amenities.sort(key=lambda x: x.name)
    return render_template(
        '10-hbnb_filters.html',
        states=states,
        amenities=amenities
    )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

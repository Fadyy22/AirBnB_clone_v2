#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.teardown_appcontext
def close_session(exception):
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def list_states(id=None):
    """renders all states in html"""
    states = storage.all(State)
    amenities = storage.all(Amenity)
    render_states = []
    render_amenities = []

    for state in states.values():
        render_states.append(state)

    for amenity in amenities.values():
        render_amenities.append(amenity)

    return render_template("10-hbnb_filters.html", states=render_states,
                           amenities=render_amenities)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def close_session(exception):
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def list_states():
    """renders all states in html"""
    states = storage.all(State)
    render_states = []
    for state in states.values():
        render_states.append(state)
    return render_template("8-cities_by_states.html", states=render_states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

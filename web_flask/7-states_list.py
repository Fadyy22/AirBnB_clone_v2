#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def close_session(exception):
    storage.close()


@app.route("/states_list", strict_slashes=False)
def list_states():
    """renders all states in html"""
    states = storage.all(State)
    render_states = {}
    for key, value in states.items():
        render_states[value.id] = value.name
    return render_template("7-states_list.html", states=render_states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

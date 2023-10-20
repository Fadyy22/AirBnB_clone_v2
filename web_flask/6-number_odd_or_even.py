#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask, render_template
from markupsafe import escape


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """displays Hello HBNB! for route '/'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """displays HBNB for route '/hbnb'"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """display “C ” followed by the value of the text variable"""
    return f"C {escape(text.replace('_', ' '))}"


@app.route("/python", strict_slashes=False, defaults={"text": "is cool"})
@app.route("/python/<text>", strict_slashes=False)
def python_text(text):
    """display “Python ” followed by the value of the text variable"""
    return f"Python {escape(text.replace('_', ' '))}"


@app.route("/number/<int:n>", strict_slashes=False)
def number_n(n):
    """display “n is a number” only if n is an integer"""
    return f"{escape(n)} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """renders html page with “Number: n” only if n is an integer"""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """renders html page with “Number: n even|odd” only if n is an integer"""
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

#!/usr/bin/python3
<<<<<<< HEAD
"""Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'.
    /hbnb: Displays 'HBNB'.
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays 'HBNB'."""
=======
"""
Write a script that starts a Flask web application:
"""

from flask import Flask
app = Flask(__name__)
strict_slashes = False


@app.route("/")
def hello():
    """ root routing """
    return "Hello HBNB!"


@app.route("/hbnb")
def hello1():
    """ extension hbnb """
>>>>>>> 42c7cabb40123c7d1a5dc64d6bc33628f2b8267e
    return "HBNB"


if __name__ == "__main__":
<<<<<<< HEAD
    app.run(host="0.0.0.0")
=======
    app.run(host='0.0.0.0', port=5000)
>>>>>>> 42c7cabb40123c7d1a5dc64d6bc33628f2b8267e

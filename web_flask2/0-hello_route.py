#!/usr/bin/python3
<<<<<<< HEAD
"""Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
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
>>>>>>> 42c7cabb40123c7d1a5dc64d6bc33628f2b8267e
    return "Hello HBNB!"


if __name__ == "__main__":
<<<<<<< HEAD
    app.run(host="0.0.0.0")
=======
    app.run(host='0.0.0.0', port=5000)
>>>>>>> 42c7cabb40123c7d1a5dc64d6bc33628f2b8267e

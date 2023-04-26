#!/usr/bin/python3
<<<<<<< HEAD
"""Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    /states_list: HTML page with a list of all State objects in DBStorage.
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Displays an HTML page with a list of all State objects in DBStorage.
    States are sorted by name.
    """
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
=======
"""
Write a script that starts a Flask web application:
"""

from flask import Flask, render_template
from models import storage
app = Flask(__name__)
strict_slashes = False


@app.route("/")
def hello():
    """ root routing """
    return "Hello HBNB!"


@app.route("/hbnb")
def hello1():
    """ extension hbnb """
    return "HBNB"


@app.route("/c/<arg>")
def hello2(arg):
    """ extension c/text """
    string = "C " + arg
    return string.replace("_", " ")


@app.route("/python/")
@app.route("/python")
def hello3():
    """ extension /python """
    return "Python is cool"


@app.route("/python/<arg>")
def hello3a(arg):
    """ extension python/text """
    string = "Python " + arg
    return string.replace("_", " ")


@app.route("/number/<int:num>")
def hello4(num):
    """ extension number/<num> """

    return str(num) + " is a number"


@app.route("/number_template/<int:num>")
def hello5(num):
    return render_template('5-number.html', number=num)


@app.route("/number_odd_or_even/<int:num>")
def hello6(num):
    word = "even"
    if num % 2:
        word = "odd"
    return render_template('6-number_odd_or_even.html',
                           number=num, string=word)


@app.teardown_appcontext
def teardown_DB(response_or_exec):
    """ tears down the db """
    storage.close()


@app.route("/states_list")
def hello7():
    statesArr = list(storage.all("State").values())
    statesArr.sort(key=lambda statesArr: statesArr.name)
    return render_template('7-states_list.html', states=statesArr)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
>>>>>>> 42c7cabb40123c7d1a5dc64d6bc33628f2b8267e

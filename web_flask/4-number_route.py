#!/usr/bin/python3
"""starts a Flask web application"""

from flask import Flask

app = Flask("__name__")

@app.route('/', strict_slashes=False)
def hello():
    """return a given string"""
    return ("Hello HBNB!")

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """return string"""
    return ("HBNB")
@app.route('/c/<text>', strict_slashes=False)
def cText(text):
    """display c """
    return "C {}".format(text.replace("_", " "))

@app.route('/python', strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pythonText(text="is cool"):
    """display python by value"""
    return "python {}".format(text.replace("_", " "))

@app.route('/number/<int:n>', strict_slashes=False)
def isNumber(n):
    """display n is number"""
    if isinstance(n,int):
        return "{} is a number".format(n)
    
    if __name__ == "__main__":
        app.run(host="0.0.0.0", port=5000, debug=None)
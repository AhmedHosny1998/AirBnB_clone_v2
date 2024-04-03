#!/usr/bin/python3
"""Starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.route("/state_list", strict_slashes=False)
def display():
    """display all states in db"""
    states = storage.all()
    return render_template('7-states_list.html', states=states)

@app.teardown_appcontext
def teradown(self):
    """remove sqlalchemy session"""
    storage.close()

    if __name__ == "__main__":
        app.run(host='0.0.0.0', port=5000)
        
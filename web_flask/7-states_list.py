#!/usr/bin/python3
"""flask app
Routes:
    /states_list: HTML page 
"""
from flask import Flask
from models import storage
from flask import render_template

app = Flask(__name__)

@app.route("/states_list", strict_slashes=False)
def states_list():
    """show an HTML page forState objects 
    """
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)

@app.teardown_appcontext
def teardown(exc):
    """delete  current session."""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0")

#!/usr/bin/python3
"""flask app
Routes:
    /cities_by_states: HTML page 
"""
from flask import Flask
from models import storage
from flask import render_template

app = Flask(__name__)

@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """show an HTML page with for stat and cities.
    """
    states = storage.all("State")
    return render_template("8-cities_by_states.html", states=states)

@app.teardown_appcontext
def teardown(exc):
    """delete  current session."""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0")

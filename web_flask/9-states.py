#!/usr/bin/python3
"""flask app
Routes:
    /states: HTML page for State .
    /states/<id>: HTML page shows state
"""
from flask import Flask
from models import storage
from flask import render_template

app = Flask(__name__)

@app.route("/states", strict_slashes=False)
def states():
    """show an HTML page with  States.
    """
    states = storage.all("State")
    return render_template("9-states.html", state=states)

@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """show an HTML page with info"""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")

@app.teardown_appcontext
def teardown(exc):
    """delete current session."""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0")

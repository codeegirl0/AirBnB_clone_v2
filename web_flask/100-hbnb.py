#!/usr/bin/python3
"""
Routes:
    /hbnb: HBnB home .
"""
from flask import Flask
from models import storage
from flask import render_template

app = Flask(__name__)

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """show the main HBnB  page."""
    amenities = storage.all("Amenity")
    states = storage.all("State")
    places = storage.all("Place")
    return render_template("100-hbnb.html",
                           states=states, amenities=amenities, places=places)


@app.teardown_appcontext
def teardown(exc):
    """delete current session."""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0")

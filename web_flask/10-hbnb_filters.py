#!/usr/bin/python3
"""flask app
Routes:
    /hbnb_filters: HBnB page with filters.
"""
from flask import Flask
from models import storage
from flask import render_template

app = Flask(__name__)

@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """show the main HBnB  page."""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template("10-hbnb_filters.html",
                           states=states, amenities=amenities)

@app.teardown_appcontext
def teardown(exc):
    """delete current session."""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0")

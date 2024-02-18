#!/usr/bin/python3
"""show 'Hello HBNB!'.
    /hbnb:  Display 'HBNB'.
"""
from flask import Flask
app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_hbnb():
    """show 'Hello HBNB!'."""
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """show 'HBNB'."""
    return "HBNB"

if __name__ == "__main__":
    app.run(host="0.0.0.0")

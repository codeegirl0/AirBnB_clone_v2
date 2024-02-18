#!/usr/bin/python3
""" flask app
Routes:
    /: for 'Hello HBNB!'.
    /hbnb: for 'HBNB'.
    /c/<text>: for 'C' with value 
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

@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """show 'C' followed by the value """
    text = text.replace("_", " ")
    return "C {}".format(text)

if __name__ == "__main__":
    app.run(host="0.0.0.0")

#!/usr/bin/python3
"""flask app
Routes:
    /: show 'Hello HBNB!'.
    /hbnb: show 'HBNB'.
    /c/<text>: show 'C' followed by the txt 
    /python/(<text>): show 'Python' followed by the txt 
    /number/<n>: show 'n is a number'  if nis an number.
"""
from flask import Flask
from flask import abort

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
    """show 'C' followed by the txt 
    """
    text = text.replace("_", " ")
    return "C {}".format(text)

@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """show 'Python' followed by the txt 
    """
    text = text.replace("_", " ")
    return "Python {}".format(text)

@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """show 'n is a number'  if n is  number."""
    return "{} is a number".format(n)

if __name__ == "__main__":
    app.run(host="0.0.0.0")

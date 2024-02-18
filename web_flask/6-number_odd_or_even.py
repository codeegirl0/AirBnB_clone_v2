#!/usr/bin/python3
"""
flask app
Routes:
    /: show 'Hello HBNB!'.
    /hbnb: show 'HBNB'.
    /c/<text>: show 'C' followed by txt
    /python/(<text>): show 'Python' followed by txt
    /number/<n>: show 'n is a number' only if n number
    /number_template/<n>: show an HTML page only if n number
    /number_odd_or_even/<n>: show an HTML page only if n number
"""
from flask import Flask
from flask import render_template

app = Flask(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

@app.route("/", strict_slashes=False)
def hello_hbnb():
    """show 'Hello HBNB!'"""
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """show 'HBNB'"""
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """show 'C' followed by the value of <text>
    """
    text = text.replace("_", " ")
    return "C {}".format(text)

@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """show 'Python' followed by the value of <text>
    """
    text = text.replace("_", " ")
    return "Python {}".format(text)

@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """show 'n is a number' only if n number"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """show an HTML page  if n number
    """
    return render_template("5-number.html", n=n)

@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """show an HTML page  if n number
    """
    return render_template("6-number_odd_or_even.html", n=n)

if __name__ == "__main__":
    app.run(host="0.0.0.0")

from flask import Flask, redirect, render_template, request, flash
from counter import Counter

app = Flask(__name__)
cnt = Counter()

@app.route("/")
def index():
    return render_template("index.html", value=cnt.value)

@app.route("/increment", methods=["POST"])
def increment():
    cnt.increase()
    return redirect("/")

@app.route("/reset", methods=["POST"])
def reset():
    cnt.reset()
    return redirect("/")

@app.route("/assign", methods=["POST"])
def assign():
    try:
        value = int(request.form.get("value"))
        if value < 0:
            raise ValueError("Value can not be negative.")
    except ValueError:
        return redirect("/")
    cnt.value = value
    return redirect("/")

import flask
from flask import request, render_template

app = flask.Flask(__name__)

@app.route("/")
def index():
    return "Hello!"

@app.route("/recognise")
def recognise():
    # face = request.args["face"]
    face = request.args.get("face")
    if face is None:
        return "You didn't supply a face"
    return render_template("face.html", face = face)

app.run(debug=True)
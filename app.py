from flask import Flask
from flask import render_template

flask_app = Flask(__name__)

@flask_app.route("/")
def view_index():
   return render_template("index.jinja")


@flask_app.route("/info/")
def view_info():
    text = "Toto je info"
    return render_template("info.jinja", text = text)
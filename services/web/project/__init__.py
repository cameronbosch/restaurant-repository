from flask_sqlalchemy import SQLAlchemy
import psycopg2
import pandas as pds

import os

from werkzeug.utils import secure_filename
from flask import (
    Flask,
    jsonify,
    send_from_directory,
    request,
    redirect,
    url_for
)


app = Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)


class Restaurants(db.Model):
    __tablename__ = "restaurants"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    boro = db.Column(db.String(60), nullable=False)
    building = db.Column(db.String(30))
    street = db.Column(db.String(150))
    zip_code = db.Column(db.Numeric(5, 0))
    phone = db.Column(db.Numeric(10, 0))
    cuisine_description = db.Column(db.String(60))
    inspection_date = db.Column(db.Date())
    action = db.Column(db.Text())
    violation_code = db.Column(db.String(3))
    violation_description = db.Column(db.Text())
    critical_flag = db.Column(db.String(25))
    score = db.Column(db.Numeric(3, 0))
    grade = db.Column(db.String(2))
    grade_date = db.Column(db.Date())
    record_date = db.Column(db.Date())
    inspection_type = db.Column(db.Text())
    latitude = db.Column(db.Numeric(16, 14))
    longitude = db.Column(db.Numeric(16, 14))
    community_board = db.Column(db.Numeric(3, 0))
    council_district = db.Column(db.Numeric(3, 0))
    census_tract = db.Column(db.Numeric(5, 0))


@app.route("/")
def hello_world():
    return jsonify(hello="world")


@app.route("/static/<path:filename>")
def staticfiles(filename):
    return send_from_directory(app.config["STATIC_FOLDER"], filename)


@app.route("/media/<path:filename>")
def mediafiles(filename):
    return send_from_directory(app.config["MEDIA_FOLDER"], filename)


@app.route("/upload", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        file = request.files["file"]
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config["MEDIA_FOLDER"], filename))
    return """
    <!doctype html>
    <title>upload new File</title>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file><input type=submit value=Upload>
    </form>
    """


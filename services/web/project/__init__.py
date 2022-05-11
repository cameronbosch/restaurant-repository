from flask_sqlalchemy import SQLAlchemy
import psycopg2
import pandas as pds
from markupsafe import escape
from sqlalchemy import create_engine, text

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


@app.route("/")
def home_page():
    return """ 
    """
    

# def hello_world():
    # return jsonify(hello="world")


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
      <p><input type=file name=file><input type=submit value=Upload></P>
    </form>
    """

@app.route("/load_data", methods=["GET", "POST"])
def reload_data():
    DATABASE_URI = "postgresql://postgresuser:poster@db:5432/restaurant_db"
    db.engine.execute(f'DROP TABLE IF EXISTS restaurants;')
    db.session.commit()
    df = pds.read_csv("restaurants.csv")
    print(df.shape)
    engine = create_engine(DATABASE_URI)
    df.to_sql("restaurants", engine, index=False, if_exists="replace")
    df_output = df.to_html(max_rows=200)
    db.session.commit()
    df_column_count = 26
    text = "<!doctype html> <title>Loaded Database</title> <br> <p>Records in the database: {0} </p> <br> <br> {1}"
    return text.format(df.size / df_column_count, df_output)


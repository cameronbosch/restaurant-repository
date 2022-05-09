from flask.cli import FlaskGroup
from sqlalchemy import create_engine
from project import app, db
import psycopg2
import pandas as pds

DATABASE_URL = "$DATABASE_URL"

cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("seed_db")
def seed_db():
    df = pds.read_csv("restaurants.csv")
    engine = create_engine(DATABASE_URL)
    df.to_sql("restaurants", engine, schema="restaurantdb")
    db.session.add()
    db.session.commit()


if __name__ == "__main__":
    cli()

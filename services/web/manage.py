from flask.cli import FlaskGroup
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from project import app, db
import psycopg2
import pandas as pds

DATABASE_URL = "postgresql://postgresuser:poster@db:5432/restaurant_db"

cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("seed_db")
def seed_db():
    db.engine.execute('DROP TABLE IF EXISTS restaurants;')
    db.session.commit()
    df = pds.read_csv("restaurants.csv")
    print(df.shape)
    engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    df.to_sql("restaurants", engine, index=False)
    db.session.commit()


if __name__ == "__main__":
    cli()


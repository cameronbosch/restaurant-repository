from flask.cli import FlaskGroup
from sqlalchemy import create_engine, Table, Column, String, Integer, Numeric, Text
from sqlalchemy.ext.declarative import declarative_base
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
    db.engine.execute(f'DROP TABLE IF EXISTS restaurants;')
    db.session.commit()
    df = pds.read_csv("restaurants.csv")
    print(df.shape)
    engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    df.to_sql("restaurants", engine, index=False)
    
    
    class Restaurant(base):
        __tablename__ = "restaurants"

        id = Column(Integer, primary_key=True)
        name = Column(String(200), nullable=False)
        boro = Column(String(60), nullable=False)
        building = Column(String(30))
        street = Column(String(150))
        zip_code = Column(Numeric(5, 0))
        phone = Column(Numeric(10, 0))
        cuisine_description = Column(String(60))
        inspection_date = Column(String)
        action = Column(Text())
        violation_code = Column(String(3))
        violation_description = Column(Text())
        critical_flag = Column(String(25))
        score = Column(Numeric(3, 0))
        grade = Column(String(2))
        grade_date = Column(String)
        record_date = Column(String)
        inspection_type = Column(Text())
        latitude = Column(Numeric(16, 14))
        longitude = Column(Numeric(16, 14))
        community_board = Column(Numeric(3, 0))
        council_district = Column(Numeric(3, 0))
        census_tract = Column(Numeric(5, 0))
    df.to_sql("restaurants", db, schema="restaurant_db", if_exists="append")
    Session = sessionmaker(db)
    session = Session()
    session.add()
    session.commit()


# if __name__ == "__main__":
    # cli()

# class Restaurant(db.Model):
    # __tablename__ = "restaurants"

    # id = db.Column(db.Integer, primary_key=True)
    # name = db.Column(db.String(200), nullable=False)
    # boro = db.Column(db.String(60), nullable=False)
    # building = db.Column(db.String(30))
    # street = db.Column(db.String(150))
    # zip_code = db.Column(db.Numeric(5, 0))
    # phone = db.Column(db.Numeric(10, 0))
    # cuisine_description = db.Column(db.String(60))
    # inspection_date = db.Column(db.Date())
    # action = db.Column(db.Text())
    # violation_code = db.Column(db.String(3))
    # violation_description = db.Column(db.Text())
    # critical_flag = db.Column(db.String(25))
    # score = db.Column(db.Numeric(3, 0))
    # grade = db.Column(db.String(2))
    # grade_date = db.Column(db.Date())
    # record_date = db.Column(db.Date())
    # inspection_type = db.Column(db.Text())
    # latitude = db.Column(db.Numeric(16, 14))
    # longitude = db.Column(db.Numeric(16, 14))
    # community_board = db.Column(db.Numeric(3, 0))
    # council_district = db.Column(db.Numeric(3, 0))
    # census_tract = db.Column(db.Numeric(5, 0))


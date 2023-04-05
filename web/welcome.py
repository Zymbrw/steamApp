from flask import Flask, render_template
from utils.constants import db_conn_str
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.dbClasses import *


app = Flask(__name__)

engine = create_engine(db_conn_str)
Session = sessionmaker(bind=engine)

# Define a route for the welcome page
@app.route("/")
def welcome():
    session = Session()
    count = session.query(Item).count()
    session.close()

    # Render the welcome page with the data from the database
    return render_template("welcome.html", count=count)

if __name__ == "__main__":
    app.run()
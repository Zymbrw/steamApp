from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.dbClasses import Item
from utils.constants import *
from sqlalchemy.sql import func
# Create a SQLAlchemy engine to connect to the database
engine = create_engine(db_conn_str)

# Create a Session class for interacting with the database
Session = sessionmaker(bind=engine)

# Query the database for all items and print their attributes
session = Session()
# items = session.query(Item).all()
# for item in items:
#     print(item.market_hash_name, item.color, item.image)

count = session.query(func.count(Item.market_hash_name.distinct())).scalar()
print("Number of rows in Item table: ", count)

# Close the database session
session.close()
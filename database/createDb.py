import psycopg2
from steamApp.utils.constants import *
from steamApp.utils.functions import *
from steamApp.database.dbClasses import *
from sqlalchemy import create_engine, MetaData


# conn = psycopg2.connect(
#     dbname="SteamApp",
#     user="SteamApp_radiorush",
#     password=get_pass(),
#     host=get_server(),
#     port=get_port()
# )

#conn_string = f'postgresql://karenalo13:91CMVrdLIPka@ep-autumn-dream-433615.eu-central-1.aws.neon.tech/neondb'
print(get_db_connString())
conn = psycopg2.connect(get_db_connString())

conn.autocommit = True
cur = conn.cursor()
cur.execute(f"SELECT datname FROM pg_catalog.pg_database WHERE datname = '{get_db_name()}';")
result = cur.fetchone()

if result:
    print("Database already exists.")
else:
    # Create the database
    cur.execute(f"CREATE DATABASE {get_db_name()};")
    conn.commit()
    print("Database created.")
cur.close()
conn.close()

engine = create_engine(db_conn_str)


Base.metadata.create_all(engine)
metadata = MetaData()




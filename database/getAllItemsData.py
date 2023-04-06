from sqlalchemy import create_engine, MetaData, Table
import requests
from steamApp.utils.constants import *


engine = create_engine(db_conn_str)
metadata = MetaData()
metadata.reflect(bind=engine, only=['item'])

def insert_items_from_api(api_url, db_conn_str):
    # Connect to the database using SQLAlchemy
    engine = create_engine(db_conn_str)
    metadata = MetaData()
    item_table = Table('item', metadata, autoload_with=engine)

    # Fetch the item data from the API
    response = requests.get(api_url)
    item_data = response.json()

    with engine.begin() as conn:
        for item in item_data['results']:
            # Insert the item into the database
            if item['asset_description']["tradable"] == 1:
                insert_stmt = item_table.insert().values(
                    market_hash_name=item['hash_name'],
                    color=item['asset_description']['name_color'],
                    image=item['asset_description']['icon_url']
                )
                conn.execute(insert_stmt)

for i in range(0,20000//100):
   insert_items_from_api(f"{get_baseApiUrl()}search_descriptions=0&appid={get_appId()}&norender=1&count=20000&start={i*100}", db_conn_str)
   print("inserted " + str((i*100 + 100)) + " items.")

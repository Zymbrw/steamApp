from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from sqlalchemy.orm import sessionmaker
from steamApp.database.dbClasses import *
from steamApp.utils.functions import *
from datetime import datetime
from sqlalchemy import create_engine, MetaData, inspect, Table
import time

today = datetime.now()
#https://community.akamai.steamstatic.com/economy/image/
#/id imagine
#/62fx62f

set_path("../config.json")
engine = create_engine(f'postgresql://{get_user()}:{get_pass()}@{get_server()}/{get_db_name()}')
Session = sessionmaker(bind=engine)
session = Session()

market_hash_names = [item.market_hash_name for item in session.query(Item).all()]

print(f"Retreived {len(market_hash_names)} items from database.")
print(f"Proceed to get buy/sell orders data for these items...")

for i in range(len(market_hash_names)):
    name = market_hash_names[i]
    print(f"Item {i+1}: {name}")
    # Specify the URL of the webpage you want to open
    url = f"{get_listingsUrl()}{get_appId()}/{name}"
    selenium_service = Service(get_chromeDriver())
    selenium_service.start()
    driver = webdriver.Chrome(service=selenium_service)

    driver.get(url)

    wait_time = 10  # seconds to wait for page to load
    element_classes = ["market_commodity_orders_table", "market_commodity_orders_table"]
    wait = WebDriverWait(driver, wait_time)
    for element_class in element_classes:
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, element_class)))
    # Retrieve the HTML content of the webpage
    html_content = driver.page_source

    # Close the web browser
    driver.quit()

    soup = BeautifulSoup(html_content, 'html.parser')
    buyOrdersTable = soup.find(id='market_commodity_buyreqeusts_table')
    buyOrdersContent = buyOrdersTable.get_text()

    buy_orders_string = buyOrdersContent.split(" or")[0].replace("PriceQuantity", "")
    numbers = []
    chArr_b = buy_orders_string.split("$")
    buyOrders = []
    for s in chArr_b[1:len(chArr_b)-1]:
        chrs = s.split(".")
        value = float(chrs[0] + "." + chrs[1][:2])
        count = int(chrs[1][2:])
        buyOrders.append(BuyOrder(name, today, value, count))

    sellOrdersTable = soup.find(id='market_commodity_forsale_table')
    sellOrdersContent = sellOrdersTable.get_text()

    sell_orders_string = sellOrdersContent.split(" or")[0].replace("PriceQuantity", "")
    numbers = []
    chArr_s = sell_orders_string.split("$")
    sellOrders = []
    for s in chArr_s[1:len(chArr_s) - 1]:
        chrs = s.split(".")
        value = float(chrs[0] + "." + chrs[1][:2])
        count = int(chrs[1][2:])
        sellOrders.append(SellOrder(name, today, value, count))

    metadata = MetaData()
    metadata.reflect(bind=engine, only=['buy_order','sell_order'])
    buy_order_table = Table('buy_order', metadata, autoload_with=engine)
    sell_order_table = Table('sell_order', metadata, autoload_with=engine)


    with engine.begin() as conn:
        for item in buyOrders:
            session.add(item)
            session.commit()
        print(f"Added {len(buyOrders)} new buy orders.")
        for item in sellOrders:
            session.add(item)
            session.commit()
        print(f"Added {len(sellOrders)} new sell orders.")

    time.sleep(5)
session.close()



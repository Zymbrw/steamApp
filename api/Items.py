from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.dbClasses import *
from utils.constants import db_conn_str

engine = create_engine(db_conn_str)


def get_items():
    Session = sessionmaker(bind=engine)
    session = Session()
    items = session.query(Item).all()
    session.close()
    return items


def get_item(market_hash_name):
    Session = sessionmaker(bind=engine)
    session = Session()
    item = session.query(Item).filter(Item.market_hash_name == market_hash_name).first()
    session.close()
    return item


def get_item_latest_buy_orders(market_hash_name):
    Session = sessionmaker(bind=engine)
    session = Session()
    last_date_buy_order = session.query(BuyOrder).filter(BuyOrder.market_hash_name == market_hash_name).order_by(BuyOrder.date.desc()).first()
    buy_orders = []
    if last_date_buy_order:
        buy_orders = session.query(BuyOrder).filter(BuyOrder.market_hash_name == market_hash_name, BuyOrder.date == last_date_buy_order.date)
    session.close()
    return buy_orders


def get_item_latest_sell_orders(market_hash_name):
    Session = sessionmaker(bind=engine)
    session = Session()
    last_date_sell_order = session.query(SellOrder).filter(SellOrder.market_hash_name == market_hash_name).order_by(SellOrder.date.desc()).first()
    sell_orders = []
    if last_date_sell_order:
        sell_orders = session.query(SellOrder).filter(SellOrder.market_hash_name == market_hash_name, SellOrder.date == last_date_sell_order.date)
    session.close()
    return sell_orders



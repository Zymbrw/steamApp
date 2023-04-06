from sqlalchemy.orm import sessionmaker
from database.dbClasses import *
from sqlalchemy import create_engine, MetaData, inspect, Table, update
from utils.functions import *
from api.Items import get_item_latest_buy_orders, get_item_latest_sell_orders
from sqlalchemy.exc import IntegrityError


def do():
    set_path("../config.json")
    engine = create_engine(f'postgresql://{get_user()}:{get_pass()}@{get_server()}/{get_db_name()}')
    Session = sessionmaker(bind=engine)
    session = Session()
    metadata = MetaData()
    metadata.reflect(bind=engine, only=['item_stats'])

    market_hash_names = [item.market_hash_name for item in session.query(Item).all()]

    for name in market_hash_names:
        sell_orders = get_item_latest_sell_orders(name)
        buy_orders = get_item_latest_buy_orders(name)

        last_date = None
        if sell_orders:
            last_date = sell_orders[0].date
        else:
            if buy_orders:
                last_date = buy_orders[0].date

        avg_buy = None
        max_buy = None
        min_buy = None
        if buy_orders:
            # Calculate the average price for the array of BuyOrder objects
            sum_product = sum([buy_order.price * buy_order.quantity for buy_order in buy_orders])
            sum_quantity = sum([buy_order.quantity for buy_order in buy_orders])
            avg_buy = 0
            if sum_quantity > 0:
                avg_buy = sum_product / sum_quantity
            max_buy = max([buy_order.price for buy_order in buy_orders])
            min_buy = min([buy_order.price for buy_order in buy_orders])

        avg_sell = None
        max_sell = None
        min_sell = None
        # Calculate the average price for the array of BuyOrder objects
        if sell_orders:
            sum_product = sum([sell_order.price * sell_order.quantity for sell_order in sell_orders])
            sum_quantity = sum([sell_order.quantity for sell_order in sell_orders])
            avg_sell = 0
            if sum_quantity > 0:
                avg_sell = sum_product / sum_quantity
            max_sell = max([sell_order.price for sell_order in sell_orders])
            min_sell = min([sell_order.price for sell_order in sell_orders])

        if last_date:
            new_item_stats = ItemStats(
                market_hash_name=name,
                date=last_date,
                sellAvg=avg_sell,
                sellMin=min_sell,
                sellMax=max_sell,
                buyAvg=avg_buy,
                buyMin=min_buy,
                buyMax=max_buy
            )
            try:
                session.add(new_item_stats)
                session.commit()
            except IntegrityError:
                session.rollback()



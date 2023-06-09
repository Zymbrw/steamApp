from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Item(Base):
    __tablename__ = 'item'
    market_hash_name = Column(String, primary_key=True)
    color = Column(String)
    image = Column(String)

    def print(self):
        print(self.market_hash_name + "||" + self.image + "||" + self.color)


class SellOrder(Base):
    __tablename__ = 'sell_order'

    def __init__(self, market_hash_name, date, price, quantity):
        self.market_hash_name = market_hash_name
        self.date = date
        self.price = price
        self.quantity = quantity

    market_hash_name = Column(String, primary_key=True)
    date = Column(DateTime, primary_key=True)
    price = Column(Float, primary_key=True)
    quantity = Column(Integer)

    def print(self):
        print(self.market_hash_name + " || " + str(self.price) + " || " + str(self.quantity) + " || " + str(self.date))


class BuyOrder(Base):
    __tablename__ = 'buy_order'

    def __init__(self, market_hash_name, date, price, quantity):
        self.market_hash_name = market_hash_name
        self.date = date
        self.price = price
        self.quantity = quantity

    market_hash_name = Column(String, primary_key=True)
    date = Column(DateTime, primary_key=True)
    price = Column(Float, primary_key=True)
    quantity = Column(Integer)

    def print(self):
        print(self.market_hash_name + " || " + str(self.price) + " || " + str(self.quantity) + " || " + str(self.date))


class ItemStats(Base):
    __tablename__ = "item_stats"
    market_hash_name = Column(String, primary_key=True)
    date = Column(DateTime, primary_key=True)
    sellAvg = Column(Float)
    sellMin = Column(Float)
    sellMax = Column(Float)
    buyAvg = Column(Float)
    buyMin = Column(Float)
    buyMax = Column(Float)

    def __init__(self, market_hash_name, date, sellAvg, sellMin, sellMax, buyAvg, buyMin, buyMax):
        self.market_hash_name = market_hash_name
        self.date = date
        self.sellAvg = sellAvg
        self.sellMin = sellMin
        self.sellMax = sellMax
        self.buyAvg = buyAvg
        self.buyMin = buyMin
        self.buyMax = buyMax

    def print(self):
        print(self.market_hash_name + " || " + str(self.date))
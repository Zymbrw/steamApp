class Item:
    def __init__(self, market_hash_name, color, image):
        self.market_hash_name = market_hash_name
        self.color = color
        self.image = image

    def print(self):
        print(self.market_hash_name + "||" + self.image + "||" + self.color)


class SellOrder:
    def __init__(self, market_hash_name, date, price, quantity):
        self.market_hash_name = market_hash_name
        self.date = date
        self.price = price
        self.quantity = quantity

    def print(self):
        print(self.market_hash_name + "||" + str(self.price) + "||" + str(self.quantity) + "||" + str(self.date))


class BuyOrder:
    def __init__(self, market_hash_name, date, price, quantity):
        self.market_hash_name = market_hash_name
        self.date = date
        self.price = price
        self.quantity = quantity

    def print(self):
        print(self.market_hash_name + " || " + str(self.price) + " || " + str(self.quantity) + " || " + str(self.date))

import math
import time


class Ring(object):
    date = time.strftime("%Y-%m-%d ", time.gmtime())  # today's date "YYYY-mm-dd"
    center = 0.0

    def __init__(self, date=date, metal="Copper", radius=5.0,price=5.0, quantity=5):
        self.date = date
        self.metal = metal
        self.radius = radius
        self.price = price
        self.quantity = quantity

    def cost(self):
        return self.price * self.quantity

    def area(self):
        return math.pi * self.radius ** 2
import random
import json


def run():
    """
    Run a sample stock portfolio script
    """

    number_of_stocks = random.randint(0,100)
    number_of_days = random.randint(0,100)

    portfolio = Portfolio()
    portfolio._generate(number_of_stocks, number_of_days)

    for stock in portfolio.stocks:

        for day in range(0, number_of_days):

            rs = portfolio.relative_strength(stock, day)
            qi = portfolio.quantile_index(stock, day)

            print(f"Stock {stock} on day {day} has relative strength = {rs}, quantile {qi}")



class Stock(object):
    def __init__(self, date, name, price):
        self.date = date
        self.name = name
        self.price = price

    def value(self):
        return self.price


class Portfolio(object):

    def __init__(self):
        self.stocks = {}

    def _generate(self, number_of_stocks, number_of_days):
        for stock_index in range(0, number_of_stocks):
            self.stocks[stock_index] = [
            Stock(i, stock_index, random.randint(1,100)) 
            for i in range(0,number_of_days)
            ]

    def relative_strength(self, stock_index, day_index):
        stock_listing = self.stocks[stock_index]
        day_of_price = stock_listing[day_index-1].price

        stock_prices = [stock.price for stock in stock_listing]

        price_list_last_250_days = [0] + stock_prices[max(day_index-250,0):day_index]

        min_price_last_250_days = min(price_list_last_250_days)
        max_price_last_250_days = max(price_list_last_250_days)

        return (day_of_price - min_price_last_250_days) / (max_price_last_250_days - min_price_last_250_days + 1 * 10**-6)

    def quantile_index(self, stock_index, day_index):
        stock_listing = self.stocks[stock_index]
        stock_prices = [stock.price for stock in stock_listing]

        day_of_relative_strength = self.relative_strength(stock_index, day_index)

        strengths = []
        for index, price in enumerate(stock_prices):
            strength = self.relative_strength(stock_index, index)
            strengths.append(strength)

        sorted_strengths = sorted(strengths)

        for index, strength in enumerate(sorted_strengths):
            if strength >= day_of_relative_strength:
                return round(10*index/len(sorted_strengths))


if __name__ == "__main__":
    run()



import random
import json
import math


def run():
    """
    Run a sample stock portfolio script
    """
    
    number_of_stocks = random.randint(1, 5) # Random choice 1 through 5
    number_of_days = random.randint(250, 300) # Random choice 250 through 300

    portfolio = Portfolio()
    portfolio._generate(number_of_stocks, number_of_days)

    for stock in portfolio.stocks:

        print(f"\nStock {stock}-index prices ordered by date.")
        print(json.dumps(portfolio.stock_prices(stock)))
        
        # Don't look at day range before 250 for an accurate picture of RS
        for day in range(250, number_of_days):
        
            rs = portfolio.relative_strength(stock, day)
            qi = portfolio.quantile_index(stock, day)

            print(
                f"Stock {stock} on day {day} has relative strength = {rs:.2f}, quantile {qi}"
            )


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
        """Randomly generates a Portfolio of Stock objects given a number of 
        stocks and number of days.
        """
        for stock_index in range(0, number_of_stocks):
            self.stocks[stock_index] = [
                Stock(i, stock_index, random.randint(1, 100))
                for i in range(0, number_of_days)
            ]

    def stock_listing(self, stock_index):
        """Returns a list of Stock objects given a stock index
        """
        return self.stocks[stock_index]

    def stock_prices(self, stock_index):
        """Returns a list of Stock prices given a stock index, assume 
        pre-sorted by date index (order)
        """
        stock_listing = self.stock_listing(stock_index)
        return [stock.price for stock in stock_listing]

    def relative_strength(self, stock_index, day_index):
        """Returns a float as a result of relative strength formula
        """
        stock_listing = self.stock_listing(stock_index)
        day_of_price = stock_listing[day_index - 1].price

        stock_prices = self.stock_prices(stock_index)

        # Start with stock price 0 to ensure list length of at least 2 days 
        # are used in min/max comparison
        price_list_last_250_days = [0] + stock_prices[
            max(day_index - 250, 0) : day_index
        ]

        min_price_last_250_days = min(price_list_last_250_days)
        max_price_last_250_days = max(price_list_last_250_days)

        return (day_of_price - min_price_last_250_days) / (
            max_price_last_250_days - min_price_last_250_days + 1 * 10 ** -6
        )

    def quantile_index(self, stock_index, day_index):
        """Returns a float as a result of relative quantile index
        """
        stock_prices = self.stock_prices(stock_index)
        day_of_relative_strength = self.relative_strength(stock_index, day_index)

        strengths = []
        for index, price in enumerate(stock_prices):
            strength = self.relative_strength(stock_index, index)
            strengths.append(strength)

        sorted_strengths = sorted(strengths)

        for index, strength in enumerate(sorted_strengths):
            if strength >= day_of_relative_strength:
                return math.floor(10 * index / len(sorted_strengths))


if __name__ == "__main__":
    run()

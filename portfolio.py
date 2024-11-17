from datetime import date


class Stock():
    """
    Represent an stock that only have 2 values for test purpose, an "initial value"
    and a "end value".
    """
    def __init__(self):
        self.switch = 0
        self.values = [5, 6.187]

    def price(self, price_date):
        price = self.values[self.switch]
        self.switch = (self.switch + 1) % 2 # Switch between the hardcoded values 
        return price

class Portfolio():
    """
    Simple Portfolio class that has a collection of Stocks and a "Profit"
    method that return the "annualized return" of the portfolio between the given dates.
    """

    def __init__(self, stocks):
        self.stocks = stocks
    
    def profit(self, start_date, end_date):
        """
        Reference: https://www.investopedia.com/terms/a/annualized-total-return.asp
        """
        days_between_dates = (end_date - start_date).days
        if days_between_dates < 365:
            """
            From the previous link: 'calculating an annualized rate of return must
            be based on historical numbers.'
            """
            raise ValueError("The two dates must be at least one year apart.") 

        started_value = sum([stock.price(start_date) for stock in self.stocks])
        end_value = sum([stock.price(end_date) for stock in self.stocks])
        cumulative_return = ((end_value / started_value ) - 1)
        annualized_return = (1 + cumulative_return)**(365/days_between_dates) - 1
        return annualized_return * 100

stocks = [Stock() for i in range(0, 1)]
portfolio = Portfolio(stocks)

# Test
start_date = date(2020, 11, 1)
end_date = date(2022, 5, 30)
print("{} %".format(portfolio.profit(start_date, end_date)))

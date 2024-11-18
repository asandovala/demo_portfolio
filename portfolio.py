from datetime import date


class Stock():
    """
    Represent a stock with prices history.

    Attributes:
        prices (dict): A dictionary mapping `datetime.date` objects to prices.
    """
    def __init__(self, prices):
        self.prices = prices

    def price(self, price_date):
        if price_date not in self.prices:
            raise ValueError(f"No price available for date: {price_date}")
        return self.prices[price_date]

class Portfolio():
    """
    Simple Portfolio class that has a collection of Stocks and a "Profit"
    method that return the "annualized return" of the portfolio between the given dates.

    Attributes:
        stocks (list): A list of `Stock` objects representing the portfolio's holdings.
    """

    def __init__(self, stocks):
        self.stocks = stocks
    
    def profit(self, start_date, end_date):
        """
        Calculates the annualized return of the portfolio.

        Args:
            start_date (datetime.date): The start date of the calculation period.
            end_date (datetime.date): The end date of the calculation period.

        Returns:
            float: The annualized return.

        Reference: https://www.investopedia.com/terms/a/annualized-total-return.asp
        """
        if start_date >= end_date:
            raise ValueError("Start date must be before end date.")

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

'''
Set up a simple test.
'''
start_date = date(2020, 11, 1)
end_date = date(2022, 5, 30)
prices = {
    start_date: 5,
    end_date: 6.187
}
stocks = [Stock(prices)]
portfolio = Portfolio(stocks)

print("Annualized return: {} %".format(portfolio.profit(start_date, end_date)))

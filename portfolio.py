from datetime import datetime
import random


class Stock():
    def price(self, price_date):
        # Random float between 10 and 50
        random_number = random.uniform(10, 50)
        return random_number

class Portfolio():
    """
    A class that represent an portfolio
    """

    def __init__(self, stocks):
        """
        Initialize the Portfolio with given stocks
        """
        self.stocks = stocks

    def add_one_year(self, date_edited):
        """
        Args:
            start_date (datetime): The inital date.
            end_date (datetime): The end date.

        Return:
            A date that's one years after the given date object 
            if it exists, otherwise use the following day
            (thus changing February 29 to February 28).

        Ref: https://stackoverflow.com/questions/15741618/add-one-year-in-current-date
        """
        try:
            return date_edited.replace(year = date_edited.year + 1)
        except ValueError:
            return date_edited.replace(year = date_edited.year + 1, day=28)

    def rate_of_return(self, start_date, end_date):
        """
        Compute the rate of return given 2 dates .

        Args:
            start_date (datetime): The inital date.
            end_date (datetime): The end date.

        Returns:
            float: The rate of return between the given dates.
        """
        value_start_date = sum([stock.price(start_date) for stock in self.stocks])
        value_end_date = sum([stock.price(end_date) for stock in self.stocks])
        return ((value_end_date - value_start_date ) / value_start_date)
    
    def profit(self, start_date, end_date):
        """
        Formula ref: https://www.investopedia.com/terms/a/annualized-total-return.asp
        """
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        tmp_date = self.add_one_year(start_date)
        annual_rates = []
        total_years = 0

        while tmp_date < end_date:
            annual_rates.append(self.annual_rate(start_date, tmp_date))
            start_date = tmp_date
            tmp_date = self.add_one_year(tmp_date)
            total_years = total_years + 1

        product_annual_rates = 1
        for annual_rate in annual_rates:
            product_annual_rates = product_annual_rates * (1 + annual_rate)
        return ((product_annual_rates**(1/total_years)) - 1) * 100

stocks = [Stock() for i in range(0, 10)]
portfolio = Portfolio(stocks)
print(portfolio.profit("2020-11-12", "2025-02-28"))

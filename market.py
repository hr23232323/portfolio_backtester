import pandas as pd
import numpy as np
import random as rd

## Python file to represent the market. This module loads the historic data and gives access to the other project files
class market:

    # method to create forward historic options prices. Includes some degree of randomness
    # to mimic real world and showcase different scenarios
    def forward_price_option(self, row, ticker):
        # Contract exp date
        exp_date = str(row["Year"] + 2) + "-" + str(row["Month"])

        # contract pricing
        current_price = row[ticker + "_price"]
        strike_price = (0.75 * current_price) - rd.random()
        price_difference = current_price - strike_price
        premium = (rd.random()/float(20)) * current_price
        contract_cost = premium + price_difference

        options_details = ticker + "@" + exp_date + "@" + "{0:.2f}".format(strike_price) + "@" + "{0:.2f}".format(contract_cost)
        return options_details

    def profit(self, opt_details):
        print(opt_details)
        ticker, exp_date, strike_price, contract_cost = opt_details.split("@")
        strike_price = float(strike_price)
        contract_cost = float(contract_cost)
        year, month = exp_date.split("-")
        year = int(year)
        month = int(month)
        row = self.data[(self.data['Year'] == year) & (self.data['Month'] == month)]
        print(row)

        print(row[ticker + "_price"])
        print(strike_price)
        change_in_price = row[ticker + "_price"] - strike_price
        print(change_in_price)

    def buy_contract(self, ticker, year, month):
        row = self.data[(self.data['Year'] == year) & (self.data['Month'] == month)]
        opt_details = row[ticker + "_forward_call_details"].values[0]
        print(row)
        return(opt_details)


    def __init__(self):
        historic_data = pd.read_csv("historic_data.csv")
        historic_data["QQQ_forward_call_details"] = historic_data.apply(lambda row: self.forward_price_option(row, "QQQ"), axis=1)
        historic_data["VTI_forward_call_details"] = historic_data.apply(lambda row: self.forward_price_option(row, "VTI"), axis=1)
        self.data =historic_data




market = market()
#print(market.data.head(20))
rand_year = rd.randrange(2002, 2020)
rand_month = rd.randrange(1, 13)
buy_details = market.buy_contract("QQQ", rand_year, rand_month)
market.profit(buy_details)

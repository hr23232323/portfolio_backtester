import pandas as pd
import numpy as np
from random import random as rd

## Python file to represent the market. This module loads the historic data and gives access to the other project files
class market:

    # method to create forward historic options prices. Includes some degree of randomness
    # to mimic real world and showcase different scenarios
    def forward_price_option(self, row, ticker):
        current_price = row[ticker + "_price"]
        strike_price = (0.75 * current_price) - rd()
        price_difference = current_price - strike_price
        premium = (rd()/float(20)) * current_price
        contract_cost = premium + price_difference
        return contract_cost



    def __init__(self):
        historic_data = pd.read_csv("historic_data.csv")
        historic_data["QQQ_forward_call_price"] = historic_data.apply(lambda row: self.forward_price_option(row, "QQQ"), axis=1)
        historic_data["VTI_forward_call_price"] = historic_data.apply(lambda row: self.forward_price_option(row, "VTI"), axis=1)
        self.data =historic_data




market = market()
print(market.data.head())

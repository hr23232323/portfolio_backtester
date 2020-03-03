import pandas as pd
import numpy as np

## Python file to represent the market. This module loads the historic data and gives access to the other project files
class market:

    def price_option(self, row, ticker):
        return 0

    def __init__(self):
        historic_data = pd.read_csv("historic_data.csv")
        historic_data["QQQ_call_price"] = historic_data.apply(lambda row: self.price_option(row, "QQQ"), axis=1)
        historic_data["VTI_call_price"] = historic_data.apply(lambda row: self.price_option(row, "VTI"), axis=1)
        self.data =historic_data




market = market()
print(market.data.head())

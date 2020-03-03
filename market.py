import pandas as pd
import numpy as np

## Python file to represent the market. This module loads the historic data and gives access to the other project files
class market:
    def __init__(self):
        self.historic_data = pd.read_csv("historic_data.csv")

    

market = market()
print(market.historic_data.head())

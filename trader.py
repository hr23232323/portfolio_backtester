import pandas as pd
import numpy as np
import random as rd
from market import market

class trader:
    def __init__(self, money):
        self.money = money
        self.curr_positions = []

    def open_rand_position(self, market, ticker, position_size):
        if(self.money > position_size):
            self.money -= position_size
            rand_year = rd.randrange(2002, 2018)
            rand_month = rd.randrange(1, 13)
            buy_details = market.buy_contract(ticker, rand_year, rand_month)
            self.curr_positions.append(buy_details)
        else:
            print("Sorry, not enough money to buy. Wait to close positions")

    def close_position(self):
        if(not self.curr_positions):
            print("No positions to sell")
        else:
            contract_to_sell = self.curr_positions.pop(0)
            trade_result = market.sell_contract(contract_to_sell)
            self.money += trade_result




profit_percent = float("{0:.2f}".format(np.mean(end_totals)))
print("After " + str(num_positions) + " positions over "+ str(years) +" years, profit %: " + str(profit_percent) + "%")
print("Annualized gains %: " + "{0:.2f}".format(profit_percent/float(years)) + "%")

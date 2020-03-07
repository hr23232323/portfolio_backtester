import pandas as pd
import numpy as np
import random as rd

class opt_trader:
    def __init__(self, money, position_size):
        self.money = money
        self.position_size = position_size
        self.curr_positions = []

    def open_rand_position(self, market, ticker):
        if(self.money > self.position_size):
            self.money -= self.position_size
            rand_year = rd.randrange(2002, 2018)
            rand_month = rd.randrange(1, 13)
            buy_details = market.buy_contract(ticker, rand_year, rand_month)
            self.curr_positions.append(buy_details)
        else:
            print("Sorry, not enough money to buy. Wait to close positions")

    def close_position(self, market):
        if(not self.curr_positions):
            print("No positions to sell")
        else:
            contract_to_sell = self.curr_positions.pop(0)
            trade_result = market.sell_contract(contract_to_sell)
            #print(trade_result)
            self.money += trade_result

    def print_status(self):
        print("---------------Trader status--------------")
        print("Current capital: " + str(self.money))
        print("Current positions: ")
        print(self.curr_positions)

import pandas as pd
import numpy as np
import random as rd

class stock_trader:
    def __init__(self, money, position_size):
        self.money = money
        self.position_size = position_size
        self.curr_positions = []

    def open_rand_position(self, market, ticker):
        if(self.money > self.position_size):
            self.money -= self.position_size
            rand_year = rd.randrange(2002, 2018)
            rand_month = rd.randrange(1, 13)
            buy_price = market.buy_stock(ticker, rand_year, rand_month)
            exp_date = str(rand_year+2) + "-" + str(rand_month)
            pos_details = ticker + "@" + exp_date + "@" + "{0:.2f}".format(buy_price)
            self.curr_positions.append(pos_details)
        else:
            print("Sorry, not enough money to buy. Wait to close positions")

    def close_position(self, market):
        if(not self.curr_positions):
            print("No positions to sell")
        else:
            stock_to_sell = self.curr_positions.pop(0)
            trade_result = market.sell_stock(stock_to_sell)
            #print(trade_result)
            self.money += trade_result

    def print_status(self):
        print("---------------Trader status--------------")
        print("Current capital: " + str(self.money))
        print("Current positions: ")
        print(self.curr_positions)

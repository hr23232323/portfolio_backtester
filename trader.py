import pandas as pd
import numpy as np
import random as rd
from market import market

class trader:
    def __init__(self, money):
        self.money = money

    def open_rand_position(self, market, ticker, position_size):
        if(self.money > position_size):
            self.money -= position_size
            rand_year = rd.randrange(2002, 2018)
            rand_month = rd.randrange(1, 13)
            buy_details = market.buy_contract(ticker, rand_year, rand_month)
        else:
            print("Sorry, not enough money to buy. Wait to close positions")

    

market = market()
#print(market.data.head(20))
initial_capital = 100000
position_percent = 0.2
position = initial_capital * position_percent
years = 1
num_positions = years * 1
end_totals = []
for i in range(years):
    percent_outcomes = []
    net_outcomes = []
    position_total = 0
    for i in range(num_positions):
        position_total +=position
        rand_year = rd.randrange(2002, 2018)
        rand_month = rd.randrange(1, 13)
        buy_details = market.buy_contract("QQQ", rand_year, rand_month)
        profit_percent = market.profit_percent(buy_details)
        #print(profit_percent)
        net_profit = position + (position * (profit_percent/float(100)))
        print(position, net_profit)
        percent_outcomes.append(profit_percent)
        net_outcomes.append(net_profit)

    total_end_capital = np.sum(net_outcomes)
    print(position_total)
    print(total_end_capital)
    end_totals.append(((total_end_capital-position_total)/float(position_total))*100)

profit_percent = float("{0:.2f}".format(np.mean(end_totals)))
print("After " + str(num_positions) + " positions over "+ str(years) +" years, profit %: " + str(profit_percent) + "%")
print("Annualized gains %: " + "{0:.2f}".format(profit_percent/float(years)) + "%")

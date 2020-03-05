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
        premium = (rd.random()/float(10)) * current_price
        contract_cost = ((1/price_difference)*premium) + premium + price_difference

        options_details = ticker + "@" + exp_date + "@" + "{0:.2f}".format(strike_price) + "@" + "{0:.2f}".format(contract_cost)
        return options_details

    def profit_percent(self, opt_details):
        print(opt_details)
        ticker, exp_date, strike_price, contract_cost = opt_details.split("@")
        year, month = exp_date.split("-")
        strike_price = float(strike_price)
        contract_cost = float(contract_cost)
        year = int(year)
        month = int(month)
        row = self.data[(self.data['Year'] == year) & (self.data['Month'] == month)]
        #print("SELL:")
        print(row)

        current_price = row[ticker + "_price"].values[0]
        current_value = current_price - strike_price
        outcome_percent = float("{0:.2f}".format(((current_value/float(contract_cost))*100)-100))
        return (outcome_percent)

    def buy_contract(self, ticker, year, month):
        row = self.data[(self.data['Year'] == year) & (self.data['Month'] == month)]
        opt_details = row[ticker + "_forward_call_details"].values[0]
        #print("BUY:")
        #print(row)
        return(opt_details)


    def __init__(self):
        historic_data = pd.read_csv("historic_data.csv")
        historic_data["QQQ_forward_call_details"] = historic_data.apply(lambda row: self.forward_price_option(row, "QQQ"), axis=1)
        historic_data["VTI_forward_call_details"] = historic_data.apply(lambda row: self.forward_price_option(row, "VTI"), axis=1)
        self.data =historic_data




market = market()
print(market.data.head(20))
initial_capital = 100000
position_percent = 0.2
position = initial_capital * position_percent
years = 5
num_positions = years * 4
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
print("Annualized gains %: " + "{0:.2f}".format(profit_percent/float(5)) + "%")

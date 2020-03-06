import pandas as pd
import numpy as np
import random as rd

## Python file to represent the market. This module loads the historic data and gives access to the other project files
class market:
    def __init__(self):
        historic_data = pd.read_csv("historic_data.csv")
        historic_data["QQQ_forward_call_details"] = historic_data.apply(lambda row: self.forward_price_option(row, "QQQ"), axis=1)
        historic_data["VTI_forward_call_details"] = historic_data.apply(lambda row: self.forward_price_option(row, "VTI"), axis=1)
        self.data =historic_data

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
        #print(row)

        current_price = row[ticker + "_price"].values[0]
        current_value = current_price - strike_price
        outcome_percent = float("{0:.2f}".format(((current_value/float(contract_cost))*100)-100))
        return (outcome_percent)

    def buy_contract(self, ticker, year, month, position_size=2000):
        row = self.data[(self.data['Year'] == year) & (self.data['Month'] == month)]
        opt_details = row[ticker + "_forward_call_details"].values[0]
        #print("BUY:")
        #print(row)
        return(opt_details)

    def calc_option_price(current_price, strike_price):
        price_diff = current_price - strike_price
        if(price_diff < (-1*0.1*strike_price)):
            premium_coef = 1
        #elif(price_diff)

        return current_price - strike_price

    def sell_contract(self, opt_details, position_size=2000):
        ticker, exp_date, strike_price, contract_cost = opt_details.split("@")
        year, month = exp_date.split("-")
        strike_price = float(strike_price)
        contract_cost = float(contract_cost)
        year = int(year)
        month = int(month)
        row = self.data[(self.data['Year'] == year) & (self.data['Month'] == month)]
        #print("SELL:")
        #print(row)

        current_price = row[ticker + "_price"].values[0]
        current_value = self.calc_option_price(current_price, strike_price)
        #print(str(current_price) + " , " + str(strike_price))
        #print(current_value)
        #print((current_value/float(contract_cost)))
        position_return = position_size * (current_value/float(contract_cost))
        return position_return

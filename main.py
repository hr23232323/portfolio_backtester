from market import market
from trader import trader
import numpy as np

def main():
    trade_market = market()
    trading_capital = 10000
    position_size = 0.2
    position_capital = trading_capital*position_size
    years = 5
    num_positions = 4
    ticker = "QQQ"
    num_exp = 100
    exp_results = []
    for e in range(num_exp):
        trader_1 = trader(trading_capital, position_capital)
        for i in range(years):
            for j in range(num_positions):
                trader_1.open_rand_position(trade_market, ticker)
            #trader_1.print_status()
            for j in range(num_positions):

                trader_1.close_position(trade_market)
            #trader_1.print_status()
        exp_results.append(((trader_1.money-trading_capital)/float(trading_capital))*100)
    mean_result = np.mean(exp_results)
    worst_result = np.min(exp_results)
    mean_profit_percent = float("{0:.2f}".format(mean_result))
    worst_profit_percent = float("{0:.2f}".format(worst_result))
    print("After " + str(num_positions*years) + " positions, mean profit %: " + str(mean_profit_percent) + "%")
    print("After " + str(num_positions*years) + " positions, worst profit %: " + str(worst_profit_percent) + "%")
if __name__ == "__main__":
    main()

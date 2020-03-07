from market import market
from stock_trader import stock_trader
from opt_trader import opt_trader
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
    exp_results_1 = []
    exp_results_2 = []
    for e in range(num_exp):
        trader_1 = opt_trader(trading_capital, position_capital)
        trader_2 = stock_trader(trading_capital, position_capital)
        for i in range(years):
            for j in range(num_positions):
                trader_1.open_rand_position(trade_market, ticker)
                trader_2.open_rand_position(trade_market, ticker)
            #trader_1.print_status()
            for j in range(num_positions):
                trader_1.close_position(trade_market)
                trader_2.close_position(trade_market)
            #trader_1.print_status()
        exp_results_1.append(((trader_1.money-trading_capital)/float(trading_capital))*100)
        exp_results_2.append(((trader_2.money-trading_capital)/float(trading_capital))*100)

def print_result(exp_results, trader_type):
    mean_result_1 = np.mean(exp_results_1)
    worst_result_1 = np.min(exp_results_1)
    mean_result_2 = np.mean(exp_results_2)
    worst_result_2 = np.min(exp_results_2)
    mean_profit_percent_1 = float("{0:.2f}".format(mean_result_1))
    worst_profit_percent_1 = float("{0:.2f}".format(worst_result_1))
    mean_profit_percent_2 = float("{0:.2f}".format(mean_result_2))
    worst_profit_percent_2 = float("{0:.2f}".format(worst_result_2))
    print("Over " + str(num_exp)+ " trials, after " + str(num_positions*years) + " positions, mean OPTION profit %: " + str(mean_profit_percent_1) + "%")
    print("Over " + str(num_exp)+ " trials, after " + str(num_positions*years) + " positions, worst OPTION profit %: " + str(worst_profit_percent_1) + "%")
    print("Over " + str(num_exp)+ " trials, after " + str(num_positions*years) + " positions, mean STOCK profit %: " + str(mean_profit_percent_2) + "%")
    print("Over " + str(num_exp)+ " trials, after " + str(num_positions*years) + " positions, worst STOCK profit %: " + str(worst_profit_percent_2) + "%")



if __name__ == "__main__":
    main()

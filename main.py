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
    ticker = "VTI"
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
    print_result(exp_results_1, num_exp, num_positions, years, "option")
    print_result(exp_results_2, num_exp, num_positions, years, "stock")

def print_result(exp_results, num_exp, num_positions, years, trader_type):
    mean_result = np.mean(exp_results)
    worst_result = np.min(exp_results)
    best_result = np.max(exp_results)
    mean_profit_percent = float("{0:.2f}".format(mean_result))
    worst_profit_percent = float("{0:.2f}".format(worst_result))
    best_profit_percent = float("{0:.2f}".format(best_result))
    print("Based on " + str(num_exp)+ " trials, after " + str(num_positions*years) + " positions over " + str(years*2) +" years, mean " + trader_type + " profit %: " + str(mean_profit_percent) + "%")
    print("Based on " + str(num_exp)+ " trials, after " + str(num_positions*years) + " positions over " + str(years*2) +" years, worst " + trader_type + " profit %: " + str(worst_profit_percent) + "%")
    print("Based on " + str(num_exp)+ " trials, after " + str(num_positions*years) + " positions over " + str(years*2) +" years, best " + trader_type + " profit %: " + str(best_profit_percent) + "%")



if __name__ == "__main__":
    main()

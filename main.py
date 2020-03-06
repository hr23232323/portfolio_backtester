from market import market
from trader import trader

def main():
    trade_market = market()
    trading_capital = 10000
    position_size = 0.2
    position_capital = trading_capital*position_size
    trader_1 = trader(trading_capital, position_capital)
    years = 5
    num_positions = 4
    ticker = "QQQ"
    for i in range(years):
        for j in range(num_positions):
            trader_1.open_rand_position(trade_market, ticker)
        #trader_1.print_status()
        for j in range(num_positions):

            trader_1.close_position(trade_market)
        #trader_1.print_status()

    profit_percent = float("{0:.2f}".format(((trader_1.money-trading_capital)/float(10000))*100))
    print("After " + str(num_positions) + " positions, profit %: " + str(profit_percent) + "%")
if __name__ == "__main__":
    main()

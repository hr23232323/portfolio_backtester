from market import market
from trader import trader

def main():
    trade_market = market()
    trader_1 = trader(10000, 2000)
    ticker = "QQQ"
    for i in range(5):
        trader_1.open_rand_position(trade_market, ticker)
        trader_1.print_status()
        trader_1.close_position(trade_market)
        trader_1.print_status()

if __name__ == "__main__":
    main()

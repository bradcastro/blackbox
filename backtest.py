import backtrader as bt
class MyStrategy(bt.Strategy):
    def __init__(self):
        # Create a moving average indicator
        self.sma = bt.indicators.SMA(self.data, period=10)
    def next(self):
        # If the price is above the moving average, buy
        if self.data.close > self.sma:
            self.buy()
        # If the price is below the moving average, sell
        elif self.data.close < self.sma:
            self.sell()
def main():
    # Create a backtest object
    cerebro = bt.Cerebro()
    # Add the strategy to the backtest object
    cerebro.addstrategy(MyStrategy)
    # Load historical data
    data = bt.feeds.PandasData(dataname='BTCUSDT.csv')
    # Add the data to the backtest object
    cerebro.adddata(data)
    # Run the backtest
    cerebro.run()
    # Print the results
    print(cerebro.broker.get_value())
if __name__ == '__main__':
    main()

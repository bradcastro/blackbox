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

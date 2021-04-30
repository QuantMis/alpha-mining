import json
import sys

class ForLoopTester:
    def __init__(self):

        # datasets
        self.data = open("Binance_ETHUSDT_5m_1 Jan, 2021-1 April, 2021.json", "r")
        self.dataset = json.loads(self.data.read())
        print("len", len(self.dataset))
        ## convert into generator
        self.dataset = (i for i in self.dataset)

        # capital and equity
        self.starting_capital = 100
        self.equity = self.starting_capital

        # volume(usdt) per trade
        self.usdt_volume = self.equity

        # trading params
        self.entryPrice = 0
        self.exitPrice = 0
        self.size = 0
        self.orderCount = 0
        self.tradesCount = 0
        self.pnlArray = []

        # exit trigger
        self.cut_loss = -1
        self.take_profit = 5

        # fees (1% of usdt per trade)
        self.fees = 0.01

    def checkBullish(self):
        for i in range(0,2):

            bar1 = next(self.dataset)
            bar2 = next(self.dataset)
            bar3 = next(self.dataset)

            if (bar1[4] < bar2[4]) and (bar2[4] < bar3[4]):
                return True
            else:
                return False

    def buyEthereum(self):
        bar = next(self.dataset)
        self.entryPrice = float(bar[1])
        self.orderCount += 1
        self.ethereum = self.equity/float(bar[1])
        print(bar[1])
        print(self.equity)
        print("size", self.ethereum)
        return 

    def sellEthereum(self, pnl):
        # update order count = 0
        # update entry price = 0
        # update ethereum = 0
        # update equity
        self.pnlArray.append(pnl)
        self.equity = self.equity + pnl
        self.entryPrice = 0
        self.ethereum = 0
        self.orderCount = 0
        self.tradesCount += 1
        return
        

    def checkPnl(self):
        # get current bar
        # compute pnl
        # check exit
        bar = next(self.dataset)
        pnl = (float(bar[1]) - self.entryPrice)*self.ethereum
        print("pml", pnl)
        if pnl > self.take_profit:
            self.sellEthereum(pnl)
        elif pnl < self.cut_loss:
            self.sellEthereum(pnl)

        return


    def main(self):
        if self.orderCount == 0:
            bullish = self.checkBullish()
            print(bullish)
            if bullish:
                self.buyEthereum()

        elif self.orderCount == 1:
           self.checkPnl()

        return

if __name__ == "__main__":
    cls = ForLoopTester()
    while True:
        try:
            cls.main()
        except StopIteration:
            print("backtest done")

            print(cls.equity)
            print(cls.tradesCount)
            print("pnlArray", cls.pnlArray)
            break


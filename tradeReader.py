class TradeReader:
    def read_trades(self, stream):
        return [line.strip() for line in stream if line.strip()]
class TradeProcessor:
    def __init__(self, reader, parser, repository):
        self.reader = reader
        self.parser = parser
        self.repository = repository

    def process_trades(self, stream):
        lines = self.reader.read_trades(stream)

        trades = []
        for i, line in enumerate(lines, start=1):
            trade = self.parser.parse(line, i)
            if trade:
                trades.append(trade)

        self.repository.save_all(trades)
        print(f"INFO: {len(trades)} trades processed")
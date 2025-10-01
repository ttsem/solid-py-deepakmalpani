class TradeParser:
    LOT_SIZE = 100000.0

    def parse(self, line, line_number):
        fields = line.split(",")

        if len(fields) != 3:
            print(f"WARN: Line {line_number} malformed. Only {len(fields)} field(s) found.")
            return None

        if len(fields[0]) != 6:
            print(f"WARN: Trade currencies on line {line_number} malformed: '{fields[0]}'")
            return None

        try:
            trade_amount = int(fields[1])
        except ValueError:
            print(f"WARN: Trade amount on line {line_number} not a valid integer: '{fields[1]}'")
            return None

        try:
            trade_price = float(fields[2])
        except ValueError:
            print(f"WARN: Trade price on line {line_number} not a valid decimal: '{fields[2]}'")
            return None

        source_currency = fields[0][:3]
        destination_currency = fields[0][3:]

        return TradeRecord(
            source_currency,
            destination_currency,
            trade_amount / self.LOT_SIZE,
            trade_price
        )

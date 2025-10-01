import pyodbc

class TradeRepository:
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def save_all(self, trades):
        with pyodbc.connect(self.connection_string) as conn:
            cursor = conn.cursor()
            try:
                for trade in trades:
                    cursor.execute(
                        "{CALL dbo.insert_trade (?, ?, ?, ?)}",
                        trade.source_currency,
                        trade.destination_currency,
                        trade.lots,
                        trade.price
                    )
                conn.commit()
            except Exception:
                conn.rollback()
                raise

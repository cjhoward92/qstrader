from qstrader.asset.asset import Asset


class CurrencyPair(Asset):
    """
    Stores metadata about a currency pair (e.g. EUR/USD)

    Parameters
    ----------
    symbol : `str`
        The currency pair symbol
    pip_decimals : `int`
        The number of decimals that represent a pip (e.g. 4 for EUR/USD, 2 for USD/JPY).
        A final decimal will automatically be added to represent a pipette.
    """

    def __init__(
            self,
            symbol,
            pip_decimals=4
    ):
        self.cash_like = False
        self.symbol = symbol
        self.pip_decimals = pip_decimals

    def __repr__(self):
        return (
            "CurrencyPair(symbol='%s', pip_decimals='%d')" % (
                self.symbol, self.pip_decimals
            )
        )

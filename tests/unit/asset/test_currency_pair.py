import pytest

from qstrader.asset.currency_pair import CurrencyPair

@pytest.mark.parametrize(
    'pair,expected,pip_decimals,expected_decimals',
    [
        ('USD/JPY', 'USD/JPY', 2, 2),
        ('EUR/USD', 'EUR/USD', 4, 4),
    ]
)
def test_currency_pair(pair, expected, pip_decimals, expected_decimals):
    """
    Tests that the currency pair is properly instantiated.
    """
    pair = CurrencyPair(pair, pip_decimals)

    assert not pair.cash_like
    assert pair.symbol == expected
    assert pair.pip_decimals == expected_decimals
import datetime
import pytest
import pytz

from qstrader.exchange.foreign_exchange import ForeignExchange


@pytest.mark.parametrize(
    'dt,expected',
    [
        # Sunday tests
        (datetime.datetime(2023, 1, 1, 20, 0, 0, 0, pytz.UTC), False),
        (datetime.datetime(2023, 1, 1, 22, 0, 0, 0, pytz.UTC), True),
        (datetime.datetime(2023, 4, 2, 20, 0, 0, 0, pytz.UTC), False),
        (datetime.datetime(2023, 4, 2, 22, 0, 0, 0, pytz.UTC), True),

        # Friday tests
        (datetime.datetime(2023, 1, 6, 21, 58, 0, 0, pytz.UTC), True),
        (datetime.datetime(2023, 1, 6, 22, 10, 0, 0, pytz.UTC), False),
        (datetime.datetime(2023, 4, 7, 21, 58, 0, 0, pytz.UTC), True),
        (datetime.datetime(2023, 4, 7, 22, 10, 0, 0, pytz.UTC), False),

        # Saturday tests
        (datetime.datetime(2023, 1, 7, 20, 0, 0, 0, pytz.UTC), False),
        (datetime.datetime(2023, 1, 7, 22, 0, 0, 0, pytz.UTC), False),
        (datetime.datetime(2023, 4, 8, 20, 0, 0, 0, pytz.UTC), False),
        (datetime.datetime(2023, 4, 8, 22, 0, 0, 0, pytz.UTC), False),

        # Thursday tests
        (datetime.datetime(2023, 1, 5, 20, 0, 0, 0, pytz.UTC), True),
        (datetime.datetime(2023, 1, 5, 22, 0, 0, 0, pytz.UTC), True),
        (datetime.datetime(2023, 4, 6, 20, 0, 0, 0, pytz.UTC), True),
        (datetime.datetime(2023, 4, 6, 22, 0, 0, 0, pytz.UTC), True),
    ]
)
def test_foreign_exchange(dt, expected):
    exchange = ForeignExchange()

    assert exchange.is_open_at_datetime(dt) == expected

import datetime
import pytz

from qstrader.exchange.exchange import Exchange


class ForeignExchange(Exchange):

    def __init__(self):
        """
        Hard-coded to represent the FX market
        opens.
        """
        self.open_t = datetime.time(21, 0)
        self.close_t = datetime.time(22, 0)

    def is_open_at_datetime(self, dt):
        """
        Check if the ForeignExchange is open at a particular
        provided pandas Timestamp.

        Parameters
        ----------
        dt : `pd.Timestamp`
            The timestamp to check for open market hours.

        Returns
        -------
        `Boolean`
            Whether the exchange is open at this timestamp.
        """
        open_dt = datetime.datetime.combine(dt.date(), self.open_t, pytz.UTC)
        close_dt = datetime.datetime.combine(dt.date(), self.close_t, pytz.UTC)
        if dt.weekday() == 6 and dt < open_dt:
            return False
        elif dt.weekday() == 4 and dt >= close_dt:
            return False
        elif dt.weekday() == 5:
            return False
        else:
            return True

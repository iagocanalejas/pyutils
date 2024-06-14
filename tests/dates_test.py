import unittest

from pyutils.strings.datetime import find_date


class TestDates(unittest.TestCase):
    def test_find_dates(self):
        dates = ["15/11/2005", "15/11/05", "25 July 2023", "29 ENERO 2023"]
        for d in dates:
            self.assertIsNotNone(find_date(d))

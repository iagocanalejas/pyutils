import pytest

from pyutils.strings.datetime import find_date


@pytest.mark.parametrize(
    ("date"),
    ["15/11/2005", "15/11/05", "25 July 2023", "29 ENERO 2023"],
)
def test_find_dates(date: str) -> None:
    assert find_date(date) is not None

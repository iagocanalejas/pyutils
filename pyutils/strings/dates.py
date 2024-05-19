import re
from datetime import date, datetime

from pyutils.strings.normalize import apply_replaces

_DAY_FIRST_DATE_FORMATS = [
    "%d-%m-%Y",
    "%d/%m/%Y",
    "%d.%m.%Y",
    "%d\\%m\\%Y",
    "%d %m %Y",
    "%d-%b-%Y",
    "%d/%b/%Y",
    "%d-%B-%Y",
    "%d/%B/%Y",
    "%d %b %Y",
    "%d %B %Y",
    "%d-%m-%y",
    "%d/%m/%y",
    "%d\\%m\\%y",
    "%d-%b-%y",
    "%d/%b/%y",
    "%d-%B-%y",
    "%d/%B/%y",
    "%d %b %y",
    "%d %B %y",
]

_DATE_FORMATS = [
    "%m %d %Y",
    "%Y-%m-%d",
    "%Y/%m/%d",
    "%Y.%m.%d",
    "%m-%d-%Y",
    "%m/%d/%Y",
    "%m.%d.%Y",
    "%b-%d-%Y",
    "%b/%d/%Y",
    "%B-%d-%Y",
    "%B/%d/%Y",
    "%b %d %Y",
    "%B %d %Y",
    "%y-%m-%d",
    "%y/%m/%d",
    "%y.%m.%d",
    "%m-%d-%y",
    "%m/%d/%y",
    "%m.%d.%y",
    "%b-%d-%y",
    "%b/%d/%y",
    "%B-%d-%y",
    "%B/%d/%y",
    "%b %d %y",
    "%B %d %y",
]


_MONTHS_MAP = {
    "01": ["ENERO", "JANUARY"],
    "02": ["FEBRERO", "FEBRUARY"],
    "03": ["MARZO", "MARCH"],
    "04": ["ABRIL", "APRIL"],
    "05": ["MAYO", "MAY"],
    "06": ["JUNIO", "JUNE"],
    "07": ["JULIO", "JULY"],
    "08": ["AGOSTO", "AUGUST"],
    "09": ["SEPTIEMBRE", "SEPTEMBER"],
    "10": ["OCTUBRE", "OCTOBER"],
    "11": ["NOVIEMBRE", "NOVEMBER"],
    "12": ["DICIEMBRE", "DECEMBER"],
}

DATE_FORMATS = _DAY_FIRST_DATE_FORMATS + _DATE_FORMATS


def find_date(maybe_date_str: str, day_first: bool | None = None) -> date | None:
    """
    :return: any matching date in the DATE_FORMATS
    """
    maybe_date_str = apply_replaces(maybe_date_str.upper(), _MONTHS_MAP)
    match = re.search(r"\b\d{1,2}[-\/.\s]\w+[-\/.\s]\d{2}\d{0,2}\b", maybe_date_str)
    if not match:
        return None

    if day_first is None:
        formats = DATE_FORMATS
    else:
        formats = _DAY_FIRST_DATE_FORMATS if day_first else _DATE_FORMATS

    maybe_date = match.group()
    for format in formats:
        try:
            return datetime.strptime(maybe_date, format).date()
        except ValueError:
            pass
    return None

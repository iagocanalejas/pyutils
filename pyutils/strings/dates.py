import re
from datetime import date, datetime
from typing import Optional

DATE_FORMATS = [
    "%d-%m-%Y",
    "%d/%m/%Y",
    "%d.%m.%Y",
    "%d\\%m\\%Y",
    "%Y-%m-%d",
    "%Y/%m/%d",
    "%Y.%m.%d",
    "%m-%d-%Y",
    "%m/%d/%Y",
    "%m.%d.%Y",
    "%d-%b-%Y",
    "%d/%b/%Y",
    "%b-%d-%Y",
    "%b/%d/%Y",
    "%d-%B-%Y",
    "%d/%B/%Y",
    "%B-%d-%Y",
    "%B/%d/%Y",
    "%d %b %Y",
    "%d %B %Y",
    "%b %d %Y",
    "%B %d %Y",
    "%d-%m-%y",
    "%d/%m/%y",
    "%d\\%m\\%y",
    "%y-%m-%d",
    "%y/%m/%d",
    "%y.%m.%d",
    "%m-%d-%y",
    "%m/%d/%y",
    "%m.%d.%y",
    "%d-%b-%y",
    "%d/%b/%y",
    "%b-%d-%y",
    "%b/%d/%y",
    "%d-%B-%y",
    "%d/%B/%y",
    "%B-%d-%y",
    "%B/%d/%y",
    "%d %b %y",
    "%d %B %y",
    "%b %d %y",
    "%B %d %y",
]


def find_date(w: str) -> Optional[date]:
    """
    :return: any matching date in the DATE_FORMATS
    """
    match = re.search(r"\b\d{1,2}[-\/.\s]\w+[-\/.\s]\d{2}\d{0,2}\b", w)
    if not match:
        return None

    date = match.group()
    for format in DATE_FORMATS:
        try:
            return datetime.strptime(date, format).date()
        except ValueError:
            pass
    return None

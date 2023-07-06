import re
from datetime import date, datetime
from typing import Optional


def find_date(w: str) -> Optional[date]:
    """
    :return: any matching date in the format of DD-MM-YYYY
    """
    match = re.search(r"([0-9]{2}-[0-9]{2}-[0-9]{4})", w)
    if not match:
        return None
    try:
        return datetime.strptime(match.group(0), '%d-%m-%Y').date()
    except ValueError:
        return None


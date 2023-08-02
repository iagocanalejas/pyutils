import re
from datetime import date, datetime
from typing import Optional


def find_date(w: str) -> Optional[date]:
    """
    :return: any matching date in the format of DD-MM-YYYY, DD/MM/YYYY and DD\\MM\\YYYY
    """
    match = re.search(r"(\d{1,2}[-\/\\]\d{1,2}[-\/\\]\d{4})", w)
    if not match:
        return None
    try:
        date = match.group(0)
        if "-" in date:
            return datetime.strptime(date, "%d-%m-%Y").date()
        if "/" in date:
            return datetime.strptime(date, "%d/%m/%Y").date()
        if "\\" in date:
            return datetime.strptime(date, "%d\\%m\\%Y").date()
    except ValueError:
        return None

from datetime import date, datetime, timedelta


def week_to_date(week: int, year: int) -> datetime:
    """
    Return datetime for the given week, year. (https://stackoverflow.com/a/17087427)

    :param week: number
    :param year: number
    :return: datetime
    """
    return datetime.fromisocalendar(year, week, 1)


def week_range_from_date(d: datetime | date) -> tuple[date, date]:
    """
    Return the first and last day of the week for the given datetime.

    :param d: A datetime object.
    :return: A tuple containing the first and last day of the week as datetime objects.
    """
    start_of_week = d - timedelta(days=d.isoweekday() - 1)
    return start_of_week, start_of_week + timedelta(days=6)


def weeks_between(d1: datetime | date, d2: datetime | date) -> timedelta:
    """
    Distance weeks between two dates. (https://stackoverflow.com/a/14191915)

    :param d1: datetime | date
    :param d2: datetime | date
    :return: timedelta
    """
    d1 = datetime.combine(d1, datetime.min.time()) if isinstance(d1, date) and not isinstance(d1, datetime) else d1
    d2 = datetime.combine(d2, datetime.min.time()) if isinstance(d2, date) and not isinstance(d2, datetime) else d2

    monday1 = d1 - timedelta(days=d1.weekday())
    monday2 = d2 - timedelta(days=d2.weekday())

    return monday2 - monday1


def date_range(start_date: date, end_date: date) -> list[date]:
    """
    Generate a list of dates between start_date and end_date (inclusive).

    :param start_date: date
    :param end_date: date
    :return: list of dates
    """
    if end_date < start_date:
        raise ValueError("end_date must be greater than or equal to start_date")
    return [start_date + timedelta(days=i) for i in range((end_date - start_date).days + 1)]

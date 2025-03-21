from datetime import date, datetime, timedelta


def week_to_date(week: int, year: int) -> datetime:
    """
    Return datetime for the given week, year. (https://stackoverflow.com/a/17087427)
    :param week: number
    :param year: number
    :return: datetime
    """
    ret = datetime.strptime(f"{year}-W{week}" + "-1", "%Y-W%W-%w")
    if date(year, 1, 4).isoweekday() > 4:
        """
        ISO defines week one to contain January 4th so the result is off by one if the first Monday and 4 January are
        in different weeks. The latter is the case if 4 January is a Friday, Saturday or Sunday.
        (https://stackoverflow.com/a/5884021)
        """
        ret -= timedelta(days=7)
    return ret


def week_range_from_date(d: datetime | date) -> tuple[date, date]:
    """
    Return the first and last day of the week for the given datetime.

    :param d: A datetime object.
    :return: A tuple containing the first and last day of the week as datetime objects.
    """
    # Get the start of the week (Monday)
    start_of_week = d - timedelta(days=d.isoweekday() - 1)
    # Get the end of the week (Sunday)
    end_of_week = start_of_week + timedelta(days=6)

    return start_of_week, end_of_week


def weeks_between(d1: datetime, d2: datetime) -> timedelta:
    """
    Distance weeks between two dates. (https://stackoverflow.com/a/14191915)
    :param d1: datetime
    :param d2: datetime
    :return: timedelta
    """
    monday1 = d1 - timedelta(days=d1.weekday())
    monday2 = d2 - timedelta(days=d2.weekday())
    return timedelta(weeks=(monday2 - monday1).days / 7)

import datetime as dt


def now_time_str():
    now = dt.datetime.now()
    return '{0:%Y%m%d%H%M%S%f}'.format(now)
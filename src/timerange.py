import datetime

import dateutil.tz


def get_time_range(days):
    EST = dateutil.tz.tzoffset('EST', -18000)  # UTC-5
    start = datetime.datetime.combine(datetime.date.today(), datetime.time(tzinfo=EST))
    end = start + datetime.timedelta(days=1, milliseconds=-1)
    start -= datetime.timedelta(days=days-1)
    tformat = '%Y-%m-%dT%H:%M:%S.%f'
    return [t.astimezone(dateutil.tz.tzutc()).strftime(tformat)[:-3]+'Z' for t in (start, end)]

for foo in (1,7,14,30):
    print(foo, get_time_range(foo))

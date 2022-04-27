# -*- coding: utf-8 -*-
'''
@File    :   time_test.py
@Time    :   2021/09/23 22:58:26
'''

import datetime as dt
max_year = dt.MAXYEAR
min_year = dt.MINYEAR
print("dt.MAXYEAR: {}".format(max_year))
print("dt.MINYEAR: {}".format(min_year))


def main():
    today = dt.date.today()
    print("today is :{}".format(today))
    year = today.year
    month = today.month
    day = today.day
    print("atoday.year:{}, atoday.month:{}, atoday.day:{}".format(year, month, day))
    get_year = today.__getattribute__('year')
    # get_year1 = today['year']
    # assert get_year == get_year1
    print("atoday.__getattribute__('year') : {}".format(get_year))

    bday = dt.date(2021, 9, 30)
    print(today > bday)

    isocalendar = today.isocalendar()
    isoformat = today.isoformat()
    weekday = today.weekday()

    print("atoday.isocalendar() : {}".format(isocalendar))
    print("atoday.isoformat() :{}".format(isoformat))
    print("atoday.weekday() :{}".format(weekday))

    timetuple = today.timetuple()
    print("atoday.timetuple() :{}".format(timetuple))
    print("atoday_timetuple.tm_year :{}".format(timetuple.tm_year))
    print("atoday_timetuple.tm_mon:{}".format(timetuple.tm_mon))
    print("atoday_timetuple.tm_mday:{}".format(timetuple.tm_mday))

    toordinal = today.toordinal()
    print("公元公历开台到现在的天数 :{}".format(toordinal))

    # replace(...)
    b = today.replace(2017, 2, 28)
    print("atoday :{}".format(today))
    print("b :{}".format(b))

    units = dt.date.resolution
    print("dt.date.resolution 日期的最小单位 :{}".format(units))
    date1 = dt.timedelta(1)
    print("dt.timedelta(1) :{}".format(date1))

    import time
    now = time.time()
    date_obj = dt.date.fromtimestamp(now)
    print("时间戮 :{}".format(now))
    print("根据时间戮返回一个日期对象 :{}".format(date_obj))

    max = dt.date.max
    min = dt.date.min
    print("dt.date.max最大日期 :{}".format(max))
    print("dt.date.min最小日期 :{}".format(min))

    print("日期的格式化输出")
    strdate = today.strftime("%Y%m%d")
    print("atoday.strftime(\"%Y%m%d\") :{}".format(strdate))

    pass


main()

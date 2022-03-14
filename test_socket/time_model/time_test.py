# -*- coding: utf-8 -*-
'''
@File    :   time_test.py
@Time    :   2021/09/23 22:58:26
'''

import datetime as dt 
print("dt.MAXYEAR: {}".format(dt.MAXYEAR))
print("dt.MINYEAR: {}".format(dt.MINYEAR))

def main():
    atoday = dt.date.today()
    print("today is :{}".format(atoday))
    print("atoday.year:{}, atoday.month:{}, atoday.day:{}".format(atoday.year, atoday.month, atoday.day))
    print("atoday.__getattribute__('year') : {}".format(atoday.__getattribute__('year')))

    bday = dt.date(2021,9,30)
    print(atoday>bday)

    print("atoday.isocalendar() : {}".format(atoday.isocalendar()))
    print("atoday.isoformat() :{}".format(atoday.isoformat()))
    print("atoday.weekday() :{}".format(atoday.weekday()))


    print("atoday.timetuple() :{}".format(atoday.timetuple()))
    atoday_timetuple = atoday.timetuple()
    print("atoday_timetuple.tm_year :{}".format(atoday_timetuple.tm_year))
    print("atoday_timetuple.tm_mon:{}".format(atoday_timetuple.tm_mon))
    print("atoday_timetuple.tm_mday:{}".format(atoday_timetuple.tm_mday))


    print("公元公历开台到现在的天数 :{}".format(atoday.toordinal()))

    # replace(...)
    b = atoday.replace(2017, 2, 28)
    print("atoday :{}".format(atoday))
    print("b :{}".format(b))


    print("dt.date.resolution 日期的最小单位 :{}".format(dt.date.resolution))
    print("dt.timedelta(1) :{}".format(dt.timedelta(1)))
    
    import time
    print("时间戮 :{}".format(time.time()))
    print("根据时间戮返回一个日期对象 :{}".format(dt.date.fromtimestamp(time.time())))

    print("dt.date.max最大日期 :{}".format(dt.date.max))
    print("dt.date.min最小日期 :{}".format(dt.date.min))

    print("日期的格式化输出")
    print("atoday.strftime(\"%Y%m%d\") :{}".format(atoday.strftime("%Y%m%d")))
    # print(" :{}".format())
    # print(" :{}".format())
    # print(" :{}".format())



    
    pass


main()
###############################################################################
# 019 Counting Sundays
'''
You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''
# 아. 영맹... 100년 동안 모든 달들.. 중에. 일요일로 시작하는 달 몇 번 있냐고?

# 일요일 0, 월요일 1, ... , 토요일 6
month = {1 : 31, 2 : 28, 3 : 31, 4 : 30, 5 : 31, 6 : 30, 7 : 31, 8 : 31, 9 : 30, 10 : 31, 11 : 30, 12 : 31}
# 요일 변화만 알고 싶으니까 7로 나눠서 나머지만 보자.
month_mod7 = { k : v % 7 for k,v in month.items()}

import copy
month_mod7_leap = copy.deepcopy(month_mod7)
month_mod7_leap [2] += 1

month_mod7_leap

day = 1 # 속았다... 1900년 1월 1일이 월요일이었던 것이다! 1901년 정보가 아니었다!
day_list = [1]

for year in range(1900, 2000 + 1):
    if year % 400 == 0:
        for v in month_mod7_leap.values():
            day += v
            day_list.append(day)          
    elif year % 100 == 0:
        for v in month_mod7.values():
            day += v
            day_list.append(day)
    elif year % 4 == 0:
        for v in month_mod7_leap.values():
            day += v
            day_list.append(day)
    else:
        for v in month_mod7.values():
            day += v
            day_list.append(day)

len(day_list) # 앞 12개는 1900년 정보, 맨 뒤 1개는 2001년 1월 1일 정보.
day_list = day_list[12:-1]
day_list_0 = [True if i % 7 == 0 else False for i in day_list]
print(sum(day_list_0)) 
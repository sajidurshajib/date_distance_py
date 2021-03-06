from sys import argv
from typing import List

# fmt: off
def app(a, b):
    old_date = date_to_int(a)
    current_date = date_to_int(b)

    years = 0
    months = 0
    days = 0

    # set date
    if current_date[0] >= old_date[0]:
        days = current_date[0] - old_date[0]
    else:
        current = current_date[0] + month_day_count(current_date[1], leap_year(current_date[2]))
        current_date[1] -= 1
        days = current - old_date[0]

    if current_date[1] >= old_date[1]:
        months = current_date[1] - old_date[1]
    else:
        months = (current_date[1] + 12) - old_date[1]
        current_date[2] -= 1

    years = current_date[2] - old_date[2]
    print('-'*25)
    print(str(days) + ' days ' + str(months) + ' months ' + str(years) + ' years ')
    print('-'*25)


def month_day_count(month: int, leap_year: bool) -> int:
    leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    not_leap = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if leap_year == True:
        return leap[month-1]
    else:
        return not_leap[month-1]


def leap_year(y: int) -> bool:
    if y % 400 == 0:
        return True
    else:
        if y % 4 == 0 and y % 100 != 0:
            return True
        else:
            return False


def date_to_int(date_str: str) -> List:
    arr = date_str.split('-')
    arr_int = []
    for x in arr:
        arr_int.append(int(x))
    return arr_int

if __name__ == '__main__':
    app(argv[1], argv[2])

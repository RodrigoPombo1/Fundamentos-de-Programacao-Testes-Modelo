def next_leap_year(year):
    leap_year_not_found = True
    while leap_year_not_found == True:
        year += 1
        if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
            return year  
def leap_year(year):
    if year % 4 == 0 and year % 400 == 0:
        if year%100 == 0:
            return f'Not a leap year'
        else:
            return f'Leap Year'

result = leap_year(2014)
print(result)
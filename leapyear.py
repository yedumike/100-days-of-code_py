"""LEAP YEAR PROGRAMME: Leap years are divisible by 4,
except for years divided by 100 only includes those also divide by 400"""

def is_leap_year(year):
    if year% 4 == 0:
        """one"""
        if year < 100:
            return True
        elif year % 100 == 0 and year % 400 == 0:
            return True
        else:
            return False
    else:
        return False
        

print(is_leap_year(2000))

"""Hello all"""
# #A year is a leap year if it is evenly divisible by 4. However, century years (ending in 00) must be divisible by 400.
# To determine if any year is a leap year according to the Gregorian calendar, it must meet one of the following conditions:

# Condition 1: The year is divisible by 400 (e.g., 1600, 2000).
# Condition 2: The year is divisible by 4 but not by 100 (e.g., 2024, 2028).

# If it meets neither of these conditions, it is a standard 365-day year. 
# For example, years like 1700, 1800, and 1900 are not leap years because they are divisible by 100 but fail the 400 division rule.
# year=int(input("enter year:"))
# if year%400==0:
#     print("year is leap year")
# elif year%4==0:
#     print("year is leap year")
# elif year%100!=0:
#     print("Year is not leap year")
# else:
#     print("Year is not leap year") 

    # "or"

# year=int(input("enter year:"))
# if (year%400==0) or (year%4==0 and year%100!=0):
#     print ("year is leap year")
# else:
#     print("year is not leap year")




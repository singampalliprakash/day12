def days_in_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return 366  # Leap year
    else:
        return 365  # Non-leap year

year = int(input("Enter a year: "))
print(f"Number of days in {year}: {days_in_year(year)}")

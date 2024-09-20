import datetime

'''# Birthday Countdown!
the_month = int(input("What month is your birthday? "))

# Get the current month and day
x = datetime.datetime.now()
current_month = int(x.strftime('%m'))
current_day = int(x.strftime('%d'))

# Calculate the months difference, adding 12 if the birthday month is in the next year
months = the_month - current_month
months = months + 12 if months < 0 else months

# Days left in the current month
days_in_month = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}

# Handle leap year for February
if current_month == 2 and x.year % 4 == 0 and (x.year % 100 != 0 or x.year % 400 == 0):
    days_in_month[2] = 29

# Calculate days remaining in the current month
days = days_in_month[current_month] - current_day

# Print the result
print(f"You have {months} month{'s' if months != 1 else ''} and {days} day{'s' if days != 1 else ''} until it's your birthday month!")'''

# --------------------------------------------------------------------------------

# New Years Resolution Check In
 
'''x = datetime.datetime.now()

month = x.strftime("%m")
day = x.strftime("%d")

print(f"It has been {month} months and {day} days since your New Years resolution. How are you doing?")'''


# --------------------------------------------------------------------------------

# The Age of Programming

'''x = datetime.datetime.now()

thisyear = x.strftime("%Y") # Capitalze the Y to maker it 2024 lower case for 24
math = int(thisyear) - 1972

print(f"It has been {math} years since the first computer program ever. Look how far we have come!")'''

# --------------------------------------------------------------------------------

# Is it a Leap Year? 

'''x = datetime.datetime.now()

time = int(x.strftime("%Y")) - 2020
calculation = time % 4
year = x.strftime("%Y")

if calculation == 0:
    print(f"This year {year}, is a leap year")
else: 
    print(f"This year {year}, is a leap year")'''

# --------------------------------------------------------------------------------

# Holidays!


x = datetime.datetime.now()
month = int(x.strftime("%m"))

if month == 1:
    print("Happy New Year!")
elif month == 2:
    print("Happy Valentine's Day or Presidents' Day!")
elif month == 3:
    print("Welcome to March! Spring is coming!")
elif month == 4:
    print("Happy Easter or Earth Day!")
elif month == 5:
    print("Happy Memorial Day!")
elif month == 6:
    print("Happy Juneteenth or Father's Day!")
elif month == 7:
    print("Happy Independence Day!")
elif month == 8:
    print("Enjoy your summer! No major holidays!")
elif month == 9:
    print("Happy Labor Day!")
elif month == 10:
    print("Happy Halloween!")
elif month == 11:
    print("Happy Thanksgiving or Veterans Day!")
elif month == 12:
    print("Merry Christmas and Happy Holidays!")
else:
    print("Enjoy this month!")











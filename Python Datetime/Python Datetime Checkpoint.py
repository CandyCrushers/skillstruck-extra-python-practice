import datetime # The import

x = datetime.datetime.now() # What makes the code word make as variable for shortness

print(x) # Prints current date and time 
print(x.strftime("%X")) # Time to the Second
print(x.strftime("%M")) # 2 Digit Month
print(x.strftime("%D")) # 2 Digit day
print(x.strftime("%Y")) # 4 Digit Year

today = datetime.date.today()
print(today) # Prints todays date
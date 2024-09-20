import math # Import math goes for all challenges 


# Biking town

'''people = int(input("How many people are in town!"))
bike = int(input("How many bikes are in town!"))

equation = people / bike  

roundit = math.ceil(equation)

print(f"In this town, for every bike that exists there are {roundit} people.")'''

# --------------------------------------------------------------------------------

# Cube Volume 

'''enter_num = int(input("Enter a number"))
print(pow(enter_num, 3))'''

# Is it a Good Investment?

'''num = int(input("How much did you buy the stock?"))
num1 = int(input("How much is the current stock?"))

x = (math.sqrt(num1 / num)-1)

print(round(x, 2)) # Round is used to round the number, the second number is by how many decimal places so 2 is by 2 decimal places!'''

# --------------------------------------------------------------------------------

# Right Triangle 

sideA = int(input("Enter a number"))
sideB = int(input("Enter a number"))

x1 = pow(sideA, 2)
x2 = pow(sideB, 2)

xTotal = x1 + x2 
xTotalsum = math.sqrt(xTotal)

print(round(xTotalsum, 2))


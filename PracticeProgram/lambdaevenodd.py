import math
from selectors import SelectSelector


num_1 = int(input("enter a number"))


result = lambda num : "Even" if num%2==0 else "odd"

print(result(num_1))



num_2 = int(input("enter a number"))

result = lambda : math.pow(int(input("enter a number\n"),2))

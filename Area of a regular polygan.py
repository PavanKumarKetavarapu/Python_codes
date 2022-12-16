s=float(input("enter the lenght of a side: "))
n=int(input("enter number of sides: "))
import math
a=(n*(s**2))/(4*(math.tan(math.pi/n)))
print("The area of a regular polygan is",a)
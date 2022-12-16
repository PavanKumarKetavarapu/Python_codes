s1=float(input("enter the length of the side 1 of the triangle: "))
s2=float(input("enter the length of the side 2 of the triangle: "))
s3=float(input("enter the length of the side 3 of the triangle: "))
s=(s1+s2+s3)/2
import math
a=math.sqrt(s*(s-s1)*(s-s2)*(s-s3))
print("the area of the triangle using side length's is",a)
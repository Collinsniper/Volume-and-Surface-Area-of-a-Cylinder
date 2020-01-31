#impotr math package to use math.pi for the value of PI 
import math
#take radius of the base of  a cylinder from user
r=float(input("Enter r of a cylinde"))
#take height of the curve surface of a cylinder from user
h=float(input("Enter the Height of a cylinde"))
#calculate the surface area of cylinder
s_area=2*math.pi*pow(r,2)*h
#calculate the volume of cylinder
volume=math.pi*pow(r,2)*h
print("surface area of a cylinder wll be %.2f" %s_area)
print("volume of a cylinder will be  %.2f" %volume)
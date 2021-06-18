import math

#The size of a car tire in the United States is represented with three numbers like this: 205/60R15. 
#The first number is the width of the tire in millimeters. 
#The second number is the aspect ratio. 
#The third number is the diameter in inches of the wheel that the tire fits.

#This function uses the formula, getting from the user the 3 variables we need
def calculate_volume(width,ratio,diameter):
    volume = float((math.pi * width**2 * ratio * (width * ratio + (2540 * diameter)))/10000000)
    return volume

width = float(input("Enter the width of the tire in mm: "))
ratio = float(input("Enter the aspect ratio of the tire: "))
diameter = float(input("Enter the diameter of the wheel in in: "))
print()
volume = calculate_volume(width, ratio, diameter)
print(f"The aproximate volume is {volume:.1f} milimeters")

#This IF statement, let's the user know if the tire is safe for using, it doesn't us
# e actual data
#I just chose those parameters. 
if volume < 30000 or volume < 25000:
        print("Your tire is not safe to use")
else:
        print("Your tire is safe to use")

import math

# Import the datatime module so that
# it can be used in this program.
from datetime import datetime

# Call the now() method to get the current date and
# time as a datetime object from the computer's clock.
current_date_and_time = datetime.now()

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
print()

#This code asks the user if they would like to buy a tire. If so, name and phone number will be requested from user
#to be contacted later, which will be displayed in the text document later

buy_tire = input("Would you like to buy a tire with this dimensions? (yes/no): ")
if buy_tire.lower() == "yes":
    print("We will save your name and phone number to contact you later")
    name = input("Please type your full name: ")
    phone_number = int(input("Please type your phone number: "))

#This code opens a new file with appending mode with all the information above
    with open("volumes.txt", "at") as volumes_file:
        print(f"Date: {current_date_and_time}", file=volumes_file)
        print(f"Width: {width}; Aspect ratio: {ratio}; Diameter: {diameter}", file=volumes_file)
        print(f"Volume: {volume:.1f} milimeters", file=volumes_file)
        print(f"{name}; {phone_number}", file=volumes_file)

else: 
    with open("volumes.txt", "at") as volumes_file:
        print(f"Date: {current_date_and_time}", file=volumes_file)
        print(f"Width: {width}; Aspect ratio: {ratio}; Diameter: {diameter}", file=volumes_file)
        print(f"Volume: {volume:.1f} milimeters", file=volumes_file)



# Import the datatime module so that
# it can be used in this program.
from datetime import datetime

# Call the now() method to get the current date and
# time as a datetime object from the computer's clock.
current = datetime.now()

# Call the isoweekday() method to get the day
# of the week from the current datetime object.
weekday = current.isoweekday()

subtotal = float(input("Please enter the subtotal: "))
tax = subtotal * .06
total = subtotal + tax
if weekday == 2 or weekday == 3:
    if subtotal >= 50:
        discount = subtotal * .10
        discount2 =subtotal - discount
        tax2 = discount2 * .06
        total2 = discount2 + tax2
        print(f"Discount amount is {discount:.2f}")
        print(f"Tax amount is {tax2:.2f}")
        print(f"Total is {total2:.2f}")
    else:
        difference = 50 - total
        print(f"Tax amount is {tax:.2f}")
        print(f"Total is {total:.2f}") 
        print("TODAY'S PROMOTION!")
        print(f"If you buy ${difference:.2f} more, you'll get a 10% discount in your subtotal")
else: 
    print(f"Tax amount is {tax:.2f}")
    print(f"Total is {total:.2f}")



import math
import random

def give_number_of_boxes(items,items_per_box):
    boxes = math.ceil(items/items_per_box)
    return boxes

random.ch

items = int(input("Enter the number of items: "))
items_per_box = int(input("Enter the number of items per box: "))
boxes = give_number_of_boxes(items, items_per_box)
print()
if boxes == 1:
    print(f"For {items} items, packing {items_per_box} in each box, you will need {boxes} box")
else:
    print(f"For {items} items, packing {items_per_box} in each box, you will need {boxes} boxes")


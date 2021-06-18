# When you physically exercise to strengthen your heart, you should maintain your heart rate within a range for at least 20 minutes. 
# To find that range, subtract your age from 220. This difference is your maximum heart rate per minute. 
# Your heart simply will not beat faster than this maximum (220 - age). When exercising to strengthen your heart, you should keep your
# heart rate between 65% and 85% of your heart's maximum.

age = int(input("Please type your age: "))
heartbeats = int(220 - age)
# Next 2 lines will find the minimum and maximum heartbeats per minute
min_heartbeats = int(heartbeats * .65) 
max_heartbeats = int(heartbeats * .85)
print("When you exercise to strengthen your heart, you should")
print(f"keep your heart rate between {min_heartbeats} and {max_heartbeats} beats per minute")
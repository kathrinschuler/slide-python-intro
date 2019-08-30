"""INSTRUCTIONS >>>
There are some problems with this code and it won't run :( Can you fix the problems so that it will run?"""

print("Is wifi available? (type y for yes, n for no")
wifi_available = input()

print("Is mobile data available? (type y for yes, n for no")
mobile_data_available = input()

if wifi_available == "y":
    print("You can get online using wifi!")
elif mobile_data_available == "y":
    print("You can get online using mobile data!")
else:
    print("You can't go online today :(")

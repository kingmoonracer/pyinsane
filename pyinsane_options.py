from src import abstract as pyinsane
from collections import OrderedDict

scanner_name = "epkowa:net:192.168.1.8"

device = pyinsane.Scanner(name=scanner_name)

# Sort the options by key into an OrderedDict dictionary
ordered_opts = OrderedDict(sorted(device.options.items(),key=lambda t: t[0]))

print("Current Options for %s") % scanner_name
print("--------------")

for key in ordered_opts:
    print("{}: {}".format(key,device.options[key].value))
    
print("--------------")
import re
import sys

number = "".join(sys.argv[1:])
number = re.sub('([\da-f-A-F]{2})' , r'.\1' , number)
number = number.split(".")
number.reverse()
number = ("".join(number))
if(number != ""):
  print(int(number,16))
else:
    print("lege invoer error ;)")
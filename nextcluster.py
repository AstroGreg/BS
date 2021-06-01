import re
import sys

startadres = int(input("First Fat adress?"), 16)
def nextcluster():
      index = int(input('index? '))
      return hex(startadres+(index*2))

def endian(number):
 number = re.sub('([\da-f-A-F]{2})' , r'.\1' , number)
 number = number.split(".")
 number.reverse()
 number = ("".join(number))
 if(number != ""):
  return int(number,16)
 else:
  return "lege invoer error ;)"
while(True):
 print(nextcluster())
 print(endian(input("convert to little endian")))
#00100800


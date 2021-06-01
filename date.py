import re

def endian(number):
 number = re.sub('([\da-f-A-F]{2})' , r'.\1' , number)
 number = number.split(".")
 number.reverse()
 number = ("".join(number))
 if(number != ""):
  return int(number,16)
 else:
  return "lege invoer error ;)"
waarde = str(bin(endian(input("geef de hex value van de tijd?")))[2:])
print(waarde)
print("vul in voor")
print("--------Results Voor tijd---------")
print("hours: " + str(int(input("hours"),2)), "minutes" +  str(int(input("minutes"),2)) , "seconds" + str(int(input("seconds"),2)*2))

#-------------------------------------------#

waarde = str(bin(endian(input("geef de hex value van de datum?")))[2:])
print(waarde)
print("--------Results Voor datum---------")
print("vul in voor")
print("year: " + str(1980 + int(input("year"),2)), "month" + str(int(input("month"),2)) , "day" + str(int(input("day"),2)))

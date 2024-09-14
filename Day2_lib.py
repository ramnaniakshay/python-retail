#string lib

myName = "aKsHay"

print(myName.upper())
print(myName.lower())

#title => after space each letter would be capital

myString = "this is helLow wORLd"
print(myString.capitalize())
print(myString.title())

#counting occurences

myString2="this  is a is a is a"
print(myString2.count('is'))

#finding a substring

myString3 = "this is hello world 3 times"
print(myString3.find('3'))

#boolean sort of function
#functions name will start with is

#isalnum
myString4="ABCD$%"
print(myString4.isalnum())

#isalpha
#isdigit

#replacing

myString5="hello world World woRld"
print(myString5.replace("world","universe"))

#splitting the text
myString6= "hello world world world 4 times"

newWord = myString6.split()
print(newWord)


#random lib
import random

#by default values are in 0 to 1 only

myRandomNumber = random.random()
print(myRandomNumber)


#run dice
get_dice = random.randint(0,7)
print(get_dice)

#Math lib library

import math

result = math.ceil(2.3)
print(result)

#floor: that will get lower value


print(math.sqrt(16))

print(math.pow(2,3))

#for loop continue keyword

#Date and time lib library

import datetime

print(datetime.datetime.now())

now = datetime.datetime.now()
print(now)

print(now.strftime("%H:%M:%S"))


today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
tomorrow= today + datetime.timedelta(days=1)
print(tomorrow)



#for loop continue keyword

for numbers in range(1,15):
    if numbers==7:
        continue
    print(numbers)





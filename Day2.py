#loops

#for loops we define condition when we want
#to stop when we want to start

#for loop

for number in range(1,11):
    print(number)

#while loop

count = 0
while count<11:
    print(count)
    #count = count + 1
    count += 1

print("Printing odd numbers using for loop")
#odd numbers using for loop

for number in range(1,11):
    if number % 2 != 0:
        print(number)

#odd and even numbers using for and while loop input function

#functions : to seprate code to logically partioned your code
        
#no parameterized function

def welcome():
    print("Welcome users to my ABC App")

welcome()

#no parameterized with return type function

def sum():
    return 5+5

#print(sum())

def addSum():
    result = sum()
    return result+5

print(addSum())


#paramterized function
def welcomeCustom(name):
    print("Welcome " , name," to my ABC app");

#name = input("Enter your name")
#welcomeCustom(name)

#multiparmaterzed function
def subtraction(numOne,numTwo):
    print("Subtraction of two numbers",numOne-numTwo)

subtraction(10,5)

#dynamically take input for two numbers and do mini calculator

#lambda function


add  = lambda x,y : x+y
result = add(5,7)
print(result)

#lambda = annoymous function
#lambda when we have small caluclations and one liner at that time we
#should consider lambda function
def findAvg(p,q,r):
    p+q+r/3

#module: module is functions of function which we can call it in any program and we can use their functions with "."

LambdaAvg = lambda firstName,lastName : firstName + lastName
result = LambdaAvg("AKS","HAY")
print(result)

import Day2_moudle

EnteredUserName = "Akshay"

print(Day2_moudle.welcome(EnteredUserName))
print(Day2_moudle.Bye(EnteredUserName))

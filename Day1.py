#Program 1
"""
This is
multi
line comment
"""
print("Hello world")

#variable program

myName = "Akshay Ramnani"
age = 1
isStudent = False
netWorth = 3.147890

"""
print(myName)
print(age)
print(isStudent)
print(netWorth)
"""

#line concation

print("Customer's name is",myName,"\nCustomer's age is ",age,"\n\t\tCutomer is student",isStudent)

#type function and conversion

x=10
y="10"
z=3.156834

print(type(x), "\n" , type(y), "\n" , type(z))

print(x+int(y))


#mini calculator
"""
1. adiition
2. subtraction
3. multiplication
4. division
\n and \t as well

"""

#input

"""
name = input("Enter your full name")
print("welcome to my ABC app",name)
"""

#string format default

"""
numOne = int(input("Enter your number"))
print(numOne)
print(type(numOne))
"""
#conditions

checkAge = 17

#normal if
if checkAge >= 18:
    print("you are and adult")


#normal if else condition
if checkAge >= 16:
    print("you are and adult")
else:
    print("you are a minor")

#multiple else if

percentage = 78

if percentage >= 90:
    print("Grade A")
elif percentage >= 80:
    print("Grade B")
else:
    print("failed")

#nested if else condition

country = "US"

if checkAge >= 16:
    if country == "US":
        print("you are an adult in US")
    else:
        print ("your adult depends on the country")
else :
    print("you are minor")

#Student report card
#to take input of student name, semester, roll number
#take marks for 3 subject Btech OS, Networking, Python
#print result \n and \t , total marks, percentage, Grade   90> A , 80> B, 70> C, failed  

x = 10
y = 20
z= 30

if x==10 and y==20 and z==50:
    print("all conditions are matched")
else:
    print("nothing is matching")



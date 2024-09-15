#list

"""
List (FILO)

->Lists in python are ordered collections of elements.
->They are mutable, you can change their elements after they are created
-> You can create list by using '[]' and it can contain any elements of different data types

"""

#fruits = ["apple","banana","orange"]
#print(fruits)

fruits = [1,2,3,"Apple","banna","orange"]

#insert after creating it
fruits.append("grapes")

#read list items
print(fruits)

#in list index starts from 0th number

#access any specific element
print(fruits[3])

#update any existing element

fruits[2] = "Watermelon"
print(fruits)

#delete an element from list
#pop method

removed_element = fruits.pop(2)
print(fruits)

#del method

my_list = [1,2,3,4,5]
del my_list[2]
print(my_list)

#slicing
#it will take starting number but it will exclude last number


my_list2 = [1,56,55,78,78,45,12,32,65,4,8,7,8,88,99,999,5,5,66,6,8,89]

sublist = my_list2[2:5]
print(sublist)

#last 3 elements printing
lastElements = my_list2[-3:]
print(lastElements)

#steping into lists
stepList = my_list2[::3]
print(stepList)



#you need to create a list of products then you should print it
#then you need to add elements,remove an element at last and then at specific index
#you need to update any existing element

#you need to use slicing


"""

Tuple

->Tuple in python are ordered collection of elements
-> tuples are imutable
-> when you create a profile and at that time(Name, dob, email)
-> once elements are created they can not be changed
-> You can create tuples by using '()' and it can contain any elements of different data types


"""



my_tuple = (1,2,3,"hello","world",67,889,90)
print(my_tuple)

print(my_tuple[-1])

#slicing that can be also applied here
#append methods are not allowed in tuple
#assignment is not allowed in tuple

#we are deleting an element by creating a new tuple

my_tuple2= (1,2,3,4,5)
print(my_tuple2[:2])
print(my_tuple2[3:])

new_tuple = my_tuple2[:2] + my_tuple2[3:]

print(new_tuple)



#list inside tuple


my_profile = [("AKshay","akshayr@cloudthat.com","1/1/2001"),10000,("123, john street, New Yourk"),"123 Banglore Karantaka"]

print(my_profile)
print(my_profile[0][0])

#you need to change salary in list and try to change name as well

#tuple inside list

#in tuple

"""

Dictionary

Dict in python are unordred collections of key pair value.
Each key is associated with its value.
so if you want to create dict then you need to us '{}'
you can change elements of dict

Except tuple we can change data types of all elments in python


"""





my_dict = { "name" : "Akshay" , "age" : 33, "city" : "New Yourk" }
print(my_dict)

#you want to access any specific value
print(my_dict["name"])

#update an element

my_dict["city"] = "Mumbai"
my_dict["city"] = "mumbai"


#insert an key pair value

my_dict["country"] = "India"
print(my_dict)

#how to remove an element

del my_dict["city"]
print(my_dict)


















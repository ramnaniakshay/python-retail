#main logic login system
#dashboard options are which are available


#break and continue function in loop

#return type of function
def main_menu():
    #all the menus drscription
    print("Welcome users to our AUthnetication system")
    print(" Press 1 for Login")
    print(" Press 2 for exit")
    choice = int(input("Enter your choice : "))
    return choice

def login():
    username=input("Enter your username")
    password=input("Enter your password")
    if username=="admin" and password=="admin":
        print("You have succesfully logedin")
        break
    else:
        print("please provide correct credentials")

#we will write one loop which will terminate on user input

while True:
    choice = main_menu()
    if choice == 1:
        login()
    elif choice == 2:
        print("exiting from this app")
        break
    else:
        print("Invalid choice please try again")

#mini calculator
# we will wask for two inputs
# we want to check '+' => addition '-' subtraction and * /
#make sure you are keeping code in functions

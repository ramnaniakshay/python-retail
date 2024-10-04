#geometry => which defines height and width of a window

#we are trying to create a addition program
#grid => one of the layout which helps you to arrange your components
#Button => which is normal button
#label => which is going to stay before input
#entry  => which is like input text
#Menu => which creates menu in ribbon side

from tkinter import *

top = Tk()

top.geometry("500x200")
#bydefault it comes with pixels

#this is our backend
def add_number():
    numOne = int(entryOne.get())
    numTwo = int(entryTwo.get())
    result = numOne+numTwo
    labelOutput.config(text=result)
    
#this is our frontend

#menu code

menu_bar= Menu(top)
top.config(menu=menu_bar)

#menu items

file_menu = Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="File", menu= file_menu)
file_menu.add_command(label="Addition",command=add_number)


labelOne = Label(top, text = "Enter the first number")
labelOne.grid(row=0,column=0)
entryOne = Entry(top)
entryOne.grid(row=0,column=1)

labelTwo = Label(top, text = "Enter the second number")
labelTwo.grid(row=1,column=0)
entryTwo = Entry(top)
entryTwo.grid(row=1,column=1)

buttonOne = Button(top, text="Addition", command=add_number)
buttonOne.grid(row=2,columnspan=2)

buttonTwo = Button(top, text="Subtraction")
buttonTwo.grid(row=3,column=1)

labelOutput = Label(top, text="")
labelOutput.grid(row=4, column=0)

var = True

check_button = Checkbutton(top, text="I agree to terms and conditions",variable=var)
check_button.grid(row=5, columnspan=3)

#radio button

radio_male = Radiobutton(top, text="Male", value="male")
radio_male.grid(row=6,column=1)
radio_female = Radiobutton(top, text="feMale", value="female")
radio_female.grid(row=7,column=1)

top.mainloop()





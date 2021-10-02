
# import tkinter
from tkinter import *
from tkinter import ttk

import tkinter.messagebox
import tkinter.simpledialog

gui = tkinter.Tk()

# empty string for user's name
user = ''

# prompt user for their name
def hello_call_back():
   global user
   tkinter.messagebox.showinfo( 'Hello World!', 'Thanks for coming!')
   user = tkinter.simpledialog.askstring( 'Query:', "What's your name? Type Below:               " )
   name_call_back()

# disable hello method, prompt for entry, display in new frame
def name_call_back():
    # make available variable
    global user

    # disable initial "hello" button
    Begin['state'] = tkinter.DISABLED
    
    # create label for user entry
    enter_value=Label(greeting_frame, text= f"Hi {user}, I am Python. Please enter a value below:")
    enter_value.place(x=20, y=50)

    # create user entry field
    D = tkinter.Entry(greeting_frame, width= 40 )
    D.place(x=20, y=70)

    # create text field
    display_input=Text(response_frame)

    # empty string for user input
    user_input = ''
   
    # gets user entered value and sends it to response frame
    def input_driver():
        user_input = D.get()
        make_new_frame(user_input)

    # builds response frame and inserts user entered value
    def make_new_frame(input):
        response_frame.place(x= 20, y= 230)   
        display_input.insert('1.0', f'{user}, you entered: {input}\n')
        display_input.pack()
    
    # displays entered string in response_frame
    E = tkinter.Button(greeting_frame, text ='Ok', command = input_driver)
    E.place(x=20, y=90)

# layout frames
hello_frame = ttk.Frame(gui, width= 340, height= 460)
hello_frame['relief'] = 'raised'
hello_frame.place(x= 230, y= 20)
hello_frame.pack_propagate(False)

greeting_frame = ttk.Frame(hello_frame, width= 300, height= 200)
greeting_frame['relief'] = 'sunken'
greeting_frame.place(x= 20, y= 20)
greeting_frame.pack_propagate(False)

response_frame = ttk.Frame(hello_frame, width= 300, height= 200)
response_frame['relief'] = 'groove'
response_frame.pack_propagate(False)

# Initial 'Hello" button and beginning of name input callback chain
Begin = tkinter.Button(greeting_frame, text ='Hello', command = hello_call_back)
Begin.place(x=20, y=10)

# Object-Oriented Frame Class


class MainFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        options = {'padx': 5, 'pady': 5}

        # label
        self.label = ttk.Label(self, text='Hello, Tkinter!')
        self.label.pack(**options)

        # button
        # self.button = ttk.Button(self, text='Click Me')
        # self.button['command'] = self.button_clicked
        # self.button.pack(**options)

        # show the frame on the container
        self.pack(**options)

    # def button_clicked(self):
    #     showinfo(title='Information',
    #              message='Hello, Tkinter!')




class SectionFrame(ttk.Frame):
    def __init__(self, name, container, width, height, relief):
        super().__init__()
        self.name = name
        self.name = ttk.Frame(container, width= width, height= height)
        self.name['relief'] = relief
        self.name.place(x= placex, y= placey)
        print(name)


def place_frame():
    # test_frame4 = SectionFrame('test4', b, 30, 30, 'groove')
    createClassFrame()
    # subFrameCallback()

def createClassFrame():
    a = SectionFrame('test1', gui, 50, 100, 'groove')

# place_frame()




def subFrameCallback():
    # frame = MainFrame(test1)

    test_frame = ttk.Frame('test1', width= 10, height= 10)
    test_frame['relief'] = 'sunken'
    test_frame.place(x= 5, y= 5)
    test_frame.pack_propagate(False)

# a.place(x=20, y=500)

# b = SectionFrame('test2', gui, 50, 100, 'raised')

# c = SectionFrame('test3', gui, 50, 100, 'sunken')

# print(test3.name)




nameTest = tkinter.Button(gui, text ='Place', command = place_frame)
nameTest.place(x=20, y=10)

nameTest2 = tkinter.Button(gui, text ='Place', command = subFrameCallback)
nameTest2.place(x=20, y=30)





# new_frame = ttk.Frame(gui, width= 340, height= 150)
# new_frame['relief'] = 'groove'
# new_frame.place(x= 230, y= 500)





# Calculator

# Database Operations

# main window styling options
gui.title('Hello, Meta... Python Desktop Application')
gui.geometry('800x800')

# run program
gui.mainloop()

# END of document

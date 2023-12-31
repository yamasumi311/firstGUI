# My first GUI program
from tkinter import *

window = Tk()
window.title('My first GUI')

def hello_function(): # this function has to be defined before the button
    print('Hello World') # prints to Shell
    # change display widge to show this text
    display_area.config(text = "Hello, World", fg="yellow", bg="black")

# adding a button widget
button1 = Button(window, text="Click Me", command = hello_function)
button1.pack() # this actually places the button on the window

# adding the display area - using the local widget
display_area = Label(window, text="")
display_area.pack() # this actually places the text area on the window

# crate a canvas to put objects on the screen
canvas = Canvas(window, width=400, height=400)
canvas.pack()

# this creates a red circle at position 100,200 of size 30 by 30
circle = canvas.create_oval(100,200,130,230, fill = 'red')

# create a blue rectangle with top left at 50,50 of size 20 by 30
blue_rect = canvas.create_rectangle(50,50,70,80, fill = 'blue')

# creates text 'Welcome' in black, font Helvetica 30 at position 200,200
screen_message = canvas.create_text(200,200, text='Welcome', fill='black', font = ('Helvetica', 30))

# create an image object using the gif file
img = PhotoImage(file='greenChar.gif')
# use image object to create a canvas image at position 100,100
mychar = canvas.create_image(100,100,image = img)

# move circle to left or right based on keys
def move_circle(event):
    key = event.keysym
    if key == 'Right':
        canvas.move(circle,10,0) # change x
    elif key == 'Left':
        canvas.move(circle,-10,0) # change x

# bind keyboard input to move_circle
canvas.bind_all('<Key>', move_circle)

# function that handles mouse clicks on the character mychar
def move_character(event):
    canvas.coords(mychar, event.x, event.y)

# bind left button mouse to moving the character
canvas.bind_all('<Button-1>', move_character)


user_data = Entry(window, text='') # initial entry is blank
user_data.pack()




window.mainloop()
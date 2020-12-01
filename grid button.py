from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk() 

def myClick():
     myLabel3 = Label(root, text="Button clicked")
     myLabel3.pack()

#Step 1 -label Widget
myLabel1 = Label(root, text="Qiktech in the house")
myLabe2 = Label(root, text="Image to Text")
myButton = Button(root, text="Submit", command=myClick)

# Step 2 -showing on screen Label
# myLabel.pack()
myLabel1.pack()
myLabe2.pack()
myButton.pack()

root.mainloop()
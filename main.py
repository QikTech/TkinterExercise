from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()

#Step 1 -label Widget
myLabel = Label(root, text="Qiktech in the house")

# Step 2 -showing on screen Label
myLabel.pack()

root.mainloop()
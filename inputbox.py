from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk() 

root.title('Convert Image to text')
root.iconbitmap('E:\Programming 0.1\MLai\Image to text\Qik5.ico')

#EXIT Program
button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack( )

e = Entry(root, width=50, borderwidth=5)
e.pack()
def myClick():
     # myLabel3 = Label(root, text=e.get())
     myLabel3 = Label(root, text="hello " +e.get())
     myLabel3.pack()

#Step 1 -label Widget
myLabel1 = Label(root, text="Qiktech in the house")
myLabe2 = Label(root, text="Image to Text")
myButton = Button(root, text="Enter name", command=myClick)

# Step 2 -showing on screen Label 
# myLabel.pack()
myLabel1.pack()
myLabe2.pack()
myButton.pack()

root.mainloop()
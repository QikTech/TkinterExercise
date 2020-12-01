from tkinter import *
# import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog
import pytesseract as tess, os
tess.pytesseract.tesseract_cmd = r'C:\Users\User\AppData\Local\Tesseract-OCR\tesseract.exe'


root = Tk() 
root.geometry("500x500")
root.title('Convert Image to text')
root.iconbitmap('E:\Programming 0.1\MLai\Image to text\Qik5.ico')


#show text
def getText():
#INSERTING EXPORTED TEXT IN TEXTBOX
     text1 = Text(root)
     text1.insert(INSERT,text)
     text1.pack()

e = Entry(root, width=50, borderwidth=5)
e.pack()
def myClick():
     # myLabel3 = Label(root, text=e.get())
     myLabel3 = Label(root, text="hello ")
     myLabel3.pack()

def open():
     # global selected_image
     root.filename = filedialog.askopenfilename(initialdir="E:\Programming 0.1\MLai\Image to text",
     title="Select a file",
     filetypes=(("Png files","*.png"),("allfiles","*.*")))
     fileLabel =Label(root, text=root.filename).pack()
     #Getting selected image path
     selected_image = ImageTk.PhotoImage(Image.open(root.filename))
     #Display Image
     # image_label = Label(image=selected_image).pack()

#Select Image Button
select_button =Button(root,text="Select image", command=open).pack()


# OCR CONVERSION
img = Image.open('image.png')
text = tess.image_to_string(img)
print (text)

#Step 1 -label Widget
myButton = Button(root, text="Enter name", command=myClick, )
# Step 2 -showing on screen Label 
myButton.pack()


#SHOW TEXT
get_text_button = Button(root, text="Get Text", command=getText)
get_text_button.pack()

# GENERATE .TXT
stringToSave = input("Give us a string:") + text
fileName = input("Give us a filename: ") + ".txt"
MyFile = open(fileName, 'w')
MyFile.write(stringToSave)
MyFile.close()

os.startfile(fileName)

root.mainloop()
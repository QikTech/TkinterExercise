from tkinter import *
# import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog
import pytesseract as tess, os
from pylint.reporters import text
tess.pytesseract.tesseract_cmd = r'C:\Users\User\AppData\Local\Tesseract-OCR\tesseract.exe'

# INITIALISING TKINTER
root = Tk() 
root.geometry("500x500")
root.title('Convert Image to text')
root.iconbitmap('E:\Programming 0.1\MLai\Image to text\Qik5.ico')


#show text DEFINED
def getText():
#INSERTING EXPORTED TEXT IN TEXTBOX
     text1 = Text(root,borderwidth=5)
     text1.insert(INSERT,tesseracttext)
     text1.pack()

# selected_image = None 
tesseracttext = None
def openimg():
     # global selected_image
     global tesseracttext
     root.filename = filedialog.askopenfilename(initialdir="E:\Programming 0.1\MLai\Image to text", title="Select a file", filetypes=(("Png files","*.png"),("allfiles","*.*")))
     fileLabel =Label(root, text="|selectedImage\n"+root.filename).pack()
     #Getting selected image path
     # selected_image = ImageTk.PhotoImage(Image.open(root.filename))
     # print (selected_image)
     # print (root.filename)
     #Display Image
     # image_label = Label(image=selected_image).pack()
     path = root.filename
     img = Image.open(root.filename)
     tesseracttext = tess.image_to_string(img)

     
#Select Image Button
select_button =Button(root,text="Select image", command=openimg)
select_button.pack()


# OCR CONVERSION
# img = Image.open('image.png')
# img = Image.open(path)
# text = tess.image_to_string(img)
# print (text)

# SHOW TEXT BUTTON
get_text_button = Button(root, text="Get Text", command=getText)
get_text_button.pack()

# GENERATE .TXT
# stringToSave = input("Give us a string:") + text
# fileName = input("Give us a filename: ") + ".txt"
# MyFile = open(fileName, 'w')
# MyFile.write(stringToSave)
# MyFile.close()
# os.startfile(fileName)

root.mainloop()
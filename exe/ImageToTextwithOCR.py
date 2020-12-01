from tkinter import *
# import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog
import pytesseract as tess, os
from pylint.reporters import text
tess.pytesseract.tesseract_cmd = r'C:\Users\User\AppData\Local\Tesseract-OCR\tesseract.exe'

# INITIALISING TKINTER
root = Tk() 
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root['bg'] = '#000001'
root.title('Convert Image to text')
root.iconbitmap('E:\Programming 0.1\MLai\Image to text\exe\Qik5.ico')


#show text DEFINED
def getText():
#INSERTING EXPORTED TEXT IN TEXTBOX
     text1 = Text(root,borderwidth=5,bg='#000001',fg="#e0fbfc")
     text1.insert(INSERT,tesseracttext)
     text1.pack()

# selected_image = None 
tesseracttext = None
def openimg():
     # global selected_image
     global tesseracttext
     root.filename = filedialog.askopenfilename(initialdir="E:\Programming 0.1\MLai\Image to text", title="Select a file", filetypes=(("Png files","*.png"),("allfiles","*.*")))
     fileLabel =Label(root, text="|| SELECTED IMAGE ||\n"+root.filename).pack()
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
select_button =Button(root,text="Select Image",font =
               ('calibri', 10, 'bold'), 
                fg = '#000001',bg='#ffffff', command=openimg)
select_button.pack()


# OCR CONVERSION
# img = Image.open('image.png')
# img = Image.open(path)
# text = tess.image_to_string(img)
# print (text)

# SHOW TEXT BUTTON
get_text_button = Button(root, text="Get Text",font =
               ('calibri', 10, 'bold'), 
                fg = '#000001',bg='#ffffff', command=getText)
get_text_button.pack()


#EXIT Program
button_quit = Button(root, text="Exit Program",font =
               ('calibri', 10, 'bold'), 
                fg = '#000001',bg='#ffffff', command=root.quit)
button_quit.pack( )

# GENERATE .TXT
# stringToSave = input("Give us a string:")
# stringToSave.pack()
# fileName = input("Give us a filename: ") + ".txt"
# MyFile = open(fileName, 'w')
# MyFile.write(stringToSave)
# MyFile.close()
# os.startfile(fileName)

root.mainloop()
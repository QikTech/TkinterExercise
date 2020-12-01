from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

root = Tk() 
root.title('Convert Image to text')
#Favicon
root.iconbitmap('E:\Programming 0.1\MLai\Image to text\Qik5.ico')



# #
# fileLabel =Label(root, text=root.filename).pack()

# #Getting selected image path
# selected_image = ImageTk.PhotoImage(Image.open(root.filename))

# #Display Image
# image_label = Label(image=selected_image).pack()

#Defining Select image button
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

root.mainloop()
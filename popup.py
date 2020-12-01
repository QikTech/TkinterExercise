from tkinter import *
from tkinter import messagebox

root = Tk() 
root.title('Convert Image to text')
#Favicon
root.iconbitmap('E:\Programming 0.1\MLai\Image to text\Qik5.ico')

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

#Defining Function
def popup(): 
     messagebox.askyesno("message", "Hello")

Button(root, text="Popup", command=popup).pack()

optxt = Text(root, width=25, height=10, wrap=WORD)
optxt.pack()

textbox = Text(root, width=100, height=100)
textbox.pack()

root.mainloop()
# import pytesseract as tess
import pytesseract as tess, os
tess.pytesseract.tesseract_cmd = r'C:\Users\User\AppData\Local\Tesseract-OCR\tesseract.exe'
from PIL import Image

img = Image.open('image.png')
text = tess.image_to_string(img)

print(text)

stringToSave = input("Give us a string:") + text
fileName = input("Give us a filename: ") + ".txt"
MyFile = open(fileName, 'w')
MyFile.write(stringToSave)
MyFile.close()

os.startfile(fileName)
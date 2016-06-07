from Tkinter import *
import PIL
from PIL import Image, ImageTk, ImageDraw
from pytesseract import *

from tkFileDialog import askopenfilename
import numpy as np
import collections
import  cv2

from sklearn.cluster import KMeans
import scipy as sc
from scipy.spatial import distance

# keras
from keras.models import Sequential
from keras.layers.core import Dense,Activation
from keras.optimizers import SGD

import matplotlib.pylab as pylab

class licencePlateRecognition(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent;
        self.initialize()

    def set_Pic_path(self,text):
        img = Image.open(text)
        img = img.resize((675, 430), PIL.Image.ANTIALIAS)

        img.save('resized.jpg')

        photo = ImageTk.PhotoImage(Image.open('resized.jpg'))
        labelSlika = Label(self, image=photo)
        labelSlika.image = photo
        labelSlika.place(x=20, y=20)

        return

    def load_image(self, path):
        return cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2RGB)

    def openFile(self):
        Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
        filename = askopenfilename(initialdir="E:/Images", title="choose your file",
                                                   filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
        location = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
        #  radiSve(location)
        #dugmeSacuvaj = Button(root, text="Upisi podatke", width=20, height=5, command=lambda: prepoznavanje(ann, alphabet))
        #dugmeSacuvaj.place(x=530, y=500)
        print(filename)
        return filename

    def initialize(self):
        self.resizable(0, 0)
        self.title("Licence plate recognition software")
        self.geometry('720x600+200+200')

        fontBold = ('Arial', 12, 'bold')
        fontSerial = ('Arial', 12)
        fontTextField = ('Arial', 16)

        dugmeUcitaj = Button(self, text="Izberite sliku", width=20, height=5,
                             command=lambda: self.set_Pic_path(self.openFile()))
        dugmeUcitaj.place(x=30, y=500)


if __name__ == "__main__":
    app = licencePlateRecognition(None)
    app.mainloop()

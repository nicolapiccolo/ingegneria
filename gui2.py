import tkinter as tk
import urllib
from tkinter import filedialog
import PIL.ImageTk
from PIL import ImageTk
from infoMonumento import Info
from dataset import Dataset
from knn import Neighbors
from riconoscitore import Riconoscitore
from PIL import Image

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


from keras.preprocessing import image
import time
from urllib.request import urlopen
import webbrowser

import tkinter.font as tkFont


def callback(url):
    webbrowser.open_new(url)

def openImg(path):
    img = PIL.Image.open(path)
    img = img.resize((350, 200), PIL.Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(img)
    return photo

def openImgURl(url):
    img = PIL.Image.open(urlopen(url))
    img = img.resize((200, 150), PIL.Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(img)
    return photo

def predict(path,model):
    # print(loaded_model.layers[0].input_shape) #(None, 160, 160, 3)
    image_path = path
    img = image.load_img(image_path, target_size=(64, 64))
    plt.imshow(img)
    img = np.expand_dims(img, axis=0)
    np_image = np.array(img).astype('float32') / 255
    pred = model.predict_classes(np_image)
    return pred


def getAllProps(monumento):
    props = []

    props.append(["Indirizzo",monumento.getAddress()])
    props.append(["Cultura",monumento.getCulture()])
    props.append(["Uso" ,monumento.getUse()])
    props.append(["Stile",monumento.getStyle()])
    props.append(["Epoca",monumento.getPeriod()])
    props.append(["Architetto",monumento.getArchitect()])
    props.append(["Religione",monumento.getReligion()])
    props.append(["Diocesi",monumento.getDiocese()])
    props.append(["Materiali usati",monumento.getMaterial()])
    props.append(["Nazione",monumento.getCountry()])
    props.append(["Regione",monumento.getRegion()])
    props.append(["Posizione",monumento.getPosition()])
    props.append(["Data apertura",monumento.getDataOpening()])
    props.append(["Altezza",monumento.getHeight()])
    props.append(["Larghezza",monumento.getWidth()])
    props.append(["Sito Web",monumento.getWebsite()])
    props.append(["Visitatori annuali",monumento.getVisitors()])
    return props



root = tk.Tk()
root.geometry("1000x500")


loaded_model = tf.keras.models.load_model('monumenti.h5')


frame1=tk.Frame(root, width=200,background="Blue")
frame1.pack(side=tk.LEFT, fill=tk.BOTH,expand=True)

frame2=tk.Frame(root, width=200,background="Green")
frame2.pack(side=tk.LEFT, fill=tk.BOTH,expand=True)

frame3=tk.Frame(root, width=200,background="Cyan")
frame3.pack(side=tk.LEFT, fill=tk.BOTH,expand=True)


path = filedialog.askopenfilename()
print(path)
photo = openImg(path)
imglbl = tk.Label(frame1, image=photo)
imglbl.pack(side=tk.TOP, fill=tk.BOTH,expand=True)


monu = Dataset.getLabel(predict(path,loaded_model)[0])
monumento = Info(monu,'')


root.title("MonumentInfo: " + monu)


"""
i=0
while i<10:
    frmlbl = tk.Frame(frame2)
    frmlbl.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    tk.Label(frmlbl, text="ciao", relief=tk.RIDGE,).grid(row=i, column=0)
    tk.Label(frmlbl, text='ciaop ciap',relief=tk.RIDGE,).grid(row=i, column=1)
    i+=1
#prop = getAllProps(monumento)
r=0
"""


d = monumento.getDescription()
tk.Label(frame2, text="DESCRIZIONE: ").pack(side=tk.TOP,fill=tk.BOTH)
w = tk.Message(frame2, text=d).pack(side=tk.TOP,fill=tk.BOTH,expand=True)


prop = getAllProps(monumento)
r = 0
for p in prop:
    if len(p[1])>0:
        frmlbl = tk.Frame(frame2)
        frmlbl.pack(side=tk.TOP, fill=tk.BOTH)
        tk.Label(frmlbl, text=p[0],relief=tk.RIDGE).grid(row=r,column=0)
        tk.Label(frmlbl, text=p[1],relief=tk.RIDGE).grid(row=r,column=1)
r+=1




nn = Neighbors()
#print(nn.getAllUri(monumento.uri))

vicini = nn.getAllUri(monumento.uri)
mon1 = Info('',vicini[0])
print(vicini[0])
mon2 = Info('',vicini[1])
print(vicini[1])
mon3 = Info('',vicini[2])
print(vicini[2])

photo1 = openImgURl(nn.getImage(vicini[0]))
time.sleep(1)
photo2 = openImgURl(nn.getImage(vicini[1]))
time.sleep(1)
photo3 = openImgURl(nn.getImage(vicini[2]))
time.sleep(1)

tk.Label(frame3, text="MONUMENTI VICINI").pack(side=tk.TOP,fill=tk.BOTH)


im1 = tk.Label(frame3, text=mon1.getName(), relief=tk.RIDGE, width=50, cursor="hand2")
im1.pack(side=tk.TOP, fill=tk.BOTH)
im1.bind("<Button-1>", lambda e: callback(vicini[0]))

tk.Label(frame3, image=photo1).pack(side=tk.TOP, fill=tk.BOTH)

im2 = tk.Label(frame3, text=mon2.getName(), relief=tk.RIDGE, width=50, cursor="hand2")
im2.pack(side=tk.TOP, fill=tk.BOTH)
im2.bind("<Button-1>", lambda e: callback(vicini[1]))

tk.Label(frame3, image=photo2).pack(side=tk.TOP, fill=tk.BOTH)

im3 = tk.Label(frame3, text=mon3.getName(), relief=tk.RIDGE, width=50,cursor="hand2")
im3.pack(side=tk.TOP, fill=tk.BOTH)
im3.bind("<Button-1>", lambda e: callback(vicini[2]))

tk.Label(frame3, image=photo3).pack(side=tk.TOP, fill=tk.BOTH)


root.mainloop()




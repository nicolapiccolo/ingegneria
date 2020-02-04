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
    mywidth = 300
    wpercent = (mywidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((mywidth, hsize), PIL.Image.ANTIALIAS)

    if hsize>800:
        myheight = 500
        wpercent = (myheight / float(img.size[1]))
        wsize = int((float(img.size[0]) * float(wpercent)))
        img = img.resize((wsize, myheight), PIL.Image.ANTIALIAS)

    print(mywidth, hsize)
    photo = ImageTk.PhotoImage(img)
    return photo

def openImgURl(url):
    if len(url)>0:
        img = PIL.Image.open(urlopen(url))
        img = img.resize((200, 150), PIL.Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(img)
        return photo
    else:
        return -1

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
root.geometry("1000x650")


loaded_model = tf.keras.models.load_model('model.h5')


frame1=tk.Frame(root, width=200,background="#1976d2",borderwidth=10, relief=tk.GROOVE)
frame1.pack(side=tk.LEFT, fill=tk.BOTH,expand=True)

frame2=tk.Frame(root, width=200,background="#1976d2",borderwidth=10, relief=tk.GROOVE)
frame2.pack(side=tk.LEFT, fill=tk.BOTH,expand=True)

frame3=tk.Frame(root, width=200,background="#1976d2",borderwidth=10, relief=tk.GROOVE)
frame3.pack(side=tk.LEFT, fill=tk.BOTH,expand=True)


path = filedialog.askopenfilename()
print(path)
photo = openImg(path)

tk.Label(frame1, text="MONUMENTO SELEZIONATO:",font=("Helvetica", 15,"bold")).pack(side=tk.TOP,fill=tk.BOTH)


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
tk.Label(frame2, text="DESCRIZIONE: ",font=("Helvetica", 15,"bold")).pack(side=tk.TOP,fill=tk.BOTH)
w = tk.Message(frame2, text=d,borderwidth=5, relief=tk.RAISED).pack(side=tk.TOP,fill=tk.BOTH)


prop = getAllProps(monumento)
r = 0
site = "www.google.it"
for p in prop:
    if len(p[1])>0:
        frmlbl = tk.Frame(frame2)
        frmlbl.pack(side=tk.TOP, fill=tk.BOTH,expand=True)

        name = tk.Label(frmlbl, text=p[0],relief=tk.RIDGE,borderwidth=2,bg="#63a4ff",font=("Helvetica", 14,"bold"))
        name.grid(row=r,column=0)

        if p[0] == "Sito Web":
            value = tk.Label(frmlbl, text=p[1],relief=tk.RIDGE,cursor="hand2")
            value.grid(row=r,column=1)
            value.bind("<Button-2>", lambda e: callback(site))
            print(p[1])
        else:
            value = tk.Label(frmlbl, text=p[1], relief=tk.RIDGE)
            value.grid(row=r, column=1)
r+=1




nn = Neighbors()
#print(nn.getAllUri(monumento.uri))

vicini = nn.getAllUri(monumento.uri)



mon1 = Info('',vicini[0])
#print(vicini[0])
mon2 = Info('',vicini[1])
#print(vicini[1])
mon3 = Info('',vicini[2])
#print(vicini[2])

photo1 = openImgURl(nn.getImage(vicini[0]))
photo2 = openImgURl(nn.getImage(vicini[1]))
photo3 = openImgURl(nn.getImage(vicini[2]))


tk.Label(frame3, text="MONUMENTI VICINI",font=("Helvetica", 15,"bold")).pack(side=tk.TOP,fill=tk.BOTH)


im1 = tk.Label(frame3, text=mon1.getName(), relief=tk.RIDGE, width=50, cursor="hand2")
im1.pack(side=tk.TOP, fill=tk.BOTH)
im1.bind("<Button-1>", lambda e: callback(vicini[0]))

if photo1!= -1: tk.Label(frame3, image=photo1).pack(side=tk.TOP, fill=tk.BOTH)
else: tk.Label(frame3, text="no image retrieved").pack(side=tk.TOP, fill=tk.BOTH)

im2 = tk.Label(frame3, text=mon2.getName(), relief=tk.RIDGE, width=50, cursor="hand2")
im2.pack(side=tk.TOP, fill=tk.BOTH)
im2.bind("<Button-1>", lambda e: callback(vicini[1]))

if photo2!= -1: tk.Label(frame3, image=photo2).pack(side=tk.TOP, fill=tk.BOTH)
else:        tk.Label(frame3, text="no image retrieved").pack(side=tk.TOP, fill=tk.BOTH)


im3 = tk.Label(frame3, text=mon3.getName(), relief=tk.RIDGE, width=50,cursor="hand2")
im3.pack(side=tk.TOP, fill=tk.BOTH)
im3.bind("<Button-1>", lambda e: callback(vicini[2]))

if photo3!= -1: tk.Label(frame3, image=photo3).pack(side=tk.TOP, fill=tk.BOTH)
else:        tk.Label(frame3, text="no image retrieved").pack(side=tk.TOP, fill=tk.BOTH)

root.mainloop()




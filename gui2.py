import tkinter as tk
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

def callback(url):
    webbrowser.open_new(url)

def openImg(path):
    img = PIL.Image.open(path)
    img = img.resize((500, 350), PIL.Image.ANTIALIAS)
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
    #print("Descrizione: " + monumento.getDescription())
    props.append(["Indirizzo",monumento.getAddress()])
    time.sleep(1)
    props.append(["Cultura",monumento.getCulture()])
    time.sleep(1)
    props.append(["Uso" ,monumento.getUse()])
    time.sleep(1)
    props.append(["Stile",monumento.getStyle()])
    time.sleep(1)
    props.append(["Epoca",monumento.getPeriod()])
    time.sleep(1)
    props.append(["Architetto",monumento.getArchitect()])
    time.sleep(1)
    props.append(["Religione",monumento.getReligion()])
    time.sleep(1)
    props.append(["Diocesi",monumento.getDiocese()])
    time.sleep(1)
    props.append(["Materiali usati",monumento.getMaterial()])
    time.sleep(1)
    props.append(["Nazione",monumento.getCountry()])
    time.sleep(1)
    props.append(["Posizione",monumento.getPosition()])
    time.sleep(1)
    props.append(["Data apertura",monumento.getDataOpening()])
    time.sleep(1)
    props.append(["Altezza",monumento.getHeight()])
    time.sleep(1)
    props.append(["Larghezza",monumento.getWidth()])
    time.sleep(1)
    props.append(["Inizio",monumento.getStart()])
    time.sleep(1)
    props.append(["Sito Web",monumento.getWebsite()])
    time.sleep(1)
    props.append(["Visitatori annuali",monumento.getVisitors()])
    time.sleep(1)
    return props





master=tk.Tk()
master.geometry("1000x700")
master.update()

loaded_model = tf.keras.models.load_model('monumenti.h5')


frame1=tk.Frame(master, width=500, height=master.winfo_height(), background="Blue")
frame1.grid(row=0, column=0, padx=10)

frame2=tk.Frame(master, width=200, height=master.winfo_height(), background="Green")
frame2.grid(row=0, column=1, padx=10)

frame3=tk.Frame(master, width=300, height=master.winfo_height(), background="Yellow")
frame3.grid(row=0, column=2, padx=10)


path = filedialog.askopenfilename()
print(path)
photo = openImg(path)
tk.Label(frame1, image=photo).grid(row=0, column=0)

monu = Dataset.getLabel(predict(path,loaded_model)[0])
monumento = Info(monu)

master.title("MonumentInfo: " + monu)


prop = getAllProps(monumento)
#prop = []

r=0
for p in prop:
    if len(p[1])>0:
        tk.Label(frame2,text=p[0], relief=tk.RIDGE, width=20).grid(row=r, column=0)
        tk.Label(frame2,text=p[1], relief=tk.SUNKEN, width=35).grid(row=r, column=1)
    r=r+1


nn = Neighbors()
#print(nn.getAllUri(monumento.uri))

vicini = nn.getAllUri(monumento.uri)
print(vicini[0])
print(vicini[1])
print(vicini[2])

photo1 = openImgURl(nn.getImage(vicini[0]))
time.sleep(1)
photo2 = openImgURl(nn.getImage(vicini[1]))
time.sleep(1)
photo3 = openImgURl(nn.getImage(vicini[2]))

im1 = tk.Label(frame3, text=vicini[0], relief=tk.RIDGE, width=50, cursor="hand2")
im1.grid(row=0, column=0)
im1.bind("<Button-1>", lambda e: callback(vicini[0]))

tk.Label(frame3, image=photo1).grid(row=1, column=0, pady=20)

im2 = tk.Label(frame3, text=vicini[1], relief=tk.RIDGE, width=50, cursor="hand2")
im2.grid(row=2, column=0)
im2.bind("<Button-1>", lambda e: callback(vicini[1]))

tk.Label(frame3, image=photo2).grid(row=3, column=0, pady=20)

im3 = tk.Label(frame3, text=vicini[2], relief=tk.RIDGE, width=50,cursor="hand2")
im3.grid(row=4, column=0)
im3.bind("<Button-1>", lambda e: callback(vicini[2]))

tk.Label(frame3, image=photo3).grid(row=5, column=0, pady=20)

""""
i=0
for v in vicini:
    photos = openImgURl()
    tk.Label(frame3, image=photos).grid(row=i, column=0)
    i = i+1
"""

master.update()

#print(monu)

master.mainloop()










#panel.pack(side="bottom", fill="both", expand="yes")

import tkinter as tk
from tkinter import filedialog
import PIL.ImageTk
from PIL import ImageTk
from infoMonumento import Info
from dataset import Dataset
from riconoscitore import Riconoscitore
from PIL import Image

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


from keras.preprocessing import image


def openImg(path):
    img = PIL.Image.open(path)
    img = img.resize((500, 350), PIL.Image.ANTIALIAS)
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


def getAllProps(monu):
    monumento = Info(monu)
    props = []
    #print("Descrizione: " + monumento.getDescription())
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
    props.append(["Posizione",monumento.getPosition()])
    props.append(["Data apertura",monumento.getDataOpening()])
    props.append(["Altezza",monumento.getHeight()])
    props.append(["Larghezza",monumento.getWidth()])
    props.append(["Inizio",monumento.getStart()])
    props.append(["Sito Web",monumento.getWebsite()])
    props.append(["Visitatori annuali",monumento.getVisitors()])
    return props





master=tk.Tk()
master.geometry("800x700")
master.update()

loaded_model = tf.keras.models.load_model('monumenti.h5')


frame1=tk.Frame(master, width=500, height=master.winfo_height(), background="Blue")
frame1.grid(row=0, column=0)

frame2=tk.Frame(master, width=200, height=master.winfo_height(), background="Green")
frame2.grid(row=0, column=1)

frame3=tk.Frame(master, width=200, height=master.winfo_height(), background="Yellow")
frame3.grid(row=0, column=2)


path = filedialog.askopenfilename()
print(path)
photo = openImg(path)
lab = tk.Label(master, image=photo).grid(row=0, column=0)

monu = Dataset.getLabel(predict(path,loaded_model)[0])

master.title("MonumentInfo: " + monu)

prop = getAllProps(monu)
r=0
for p in prop:
    if(len(p[1])>0):
        tk.Label(frame2,text=p[0], relief=tk.RIDGE, width=20).grid(row=r, column=0)
        tk.Label(frame2,text=p[1], relief=tk.SUNKEN, width=35).grid(row=r, column=1)
    r=r+1

#print(monu)

master.mainloop()










#panel.pack(side="bottom", fill="both", expand="yes")

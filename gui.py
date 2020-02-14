import tkinter as tk
from tkinter import filedialog
import PIL.ImageTk
from PIL import ImageTk
from infoMonumento import Info
from dataset import Dataset
from neighbors import Neighbors
from PIL import Image

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


from keras.preprocessing import image

from urllib.request import urlopen
import webbrowser




def on_configure(event):
    canvas.configure(scrollregion=canvas.bbox('all'))

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
root.geometry("1100x650")


loaded_model = tf.keras.models.load_model('modello/mymodel.h5')
loaded_model.summary()


frame1=tk.Frame(root, width=200,background="#1976d2",borderwidth=10, relief=tk.GROOVE)
frame1.pack(side=tk.LEFT, fill=tk.Y,expand=True)


canvas = tk.Canvas(root,width=500,borderwidth=10, relief=tk.GROOVE)
canvas.pack(side=tk.LEFT, fill=tk.BOTH,expand=True)

scrollbar = tk.Scrollbar(root, command=canvas.yview)
scrollbar.pack(side=tk.LEFT, fill=tk.Y)

canvas.configure(yscrollcommand = scrollbar.set)

canvas.bind('<Configure>', on_configure)


frame2=tk.Frame(canvas)
canvas.create_window((0,0), window=frame2, anchor='nw')

frame3=tk.Frame(root, width=150,background="#1976d2",borderwidth=10, relief=tk.GROOVE)
frame3.pack(side=tk.LEFT, fill=tk.Y,expand=True)


path = filedialog.askopenfilename()
print(path)
photo = openImg(path)

monu = Dataset.getLabel(predict(path,loaded_model)[0])
monumento = Info(monu,'')

root.title("MonumentInfo: " + monu)


tk.Label(frame1, text="MONUMENTO SELEZIONATO:",font=("Helvetica", 15,"bold")).pack(side=tk.TOP,fill=tk.BOTH)
tk.Label(frame1, text=monu,font=("Helvetica", 13,"bold")).pack(side=tk.TOP,fill=tk.BOTH)



imglbl = tk.Label(frame1, image=photo)
imglbl.pack(side=tk.TOP, fill=tk.BOTH,expand=True)




d = monumento.getDescription() or monumento.getDescriptionEn()
tk.Label(frame2, text="DESCRIZIONE: ",font=("Helvetica", 15,"bold")).pack(side=tk.TOP,fill=tk.BOTH)
w = tk.Message(frame2, text=d,borderwidth=5, relief=tk.RAISED,aspect=120,width=490)
w.pack(side=tk.TOP,fill=tk.BOTH,expand=True)




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
vicini = nn.getAllUri(monumento.uri)



mon1 = Info('',vicini[0])
#print(vicini[0])
mon2 = Info('',vicini[1])
#print(vicini[1])
mon3 = Info('',vicini[2])
#print(vicini[2])

site1 = mon1.getWiki() or mon1.getWebsite()
site2 = mon2.getWiki() or mon2.getWebsite()
site3 = mon3.getWiki() or mon3.getWebsite()

geo1 = mon1.getGeolocation()
map1=f"https://maps.google.com/maps?q={geo1[0]},{geo1[1]}&hl=es;z=14&amp;output=embed"

geo2 = mon2.getGeolocation()
map2=f"https://maps.google.com/maps?q={geo2[0]},{geo2[1]}&hl=es;z=14&amp;output=embed"

geo3 = mon3.getGeolocation()
map3=f"https://maps.google.com/maps?q={geo3[0]},{geo3[1]}&hl=es;z=14&amp;output=embed"



print(map1)

photo1 = openImgURl(nn.getImage(vicini[0]))
photo2 = openImgURl(nn.getImage(vicini[1]))
photo3 = openImgURl(nn.getImage(vicini[2]))


tk.Label(frame3, text="MONUMENTI VICINI",font=("Helvetica", 15,"bold")).pack(side=tk.TOP,fill=tk.BOTH)


im1 = tk.Label(frame3, text=mon1.getName(), relief=tk.RIDGE, width=50, cursor="hand2")
im1.pack(side=tk.TOP, fill=tk.BOTH)
im1.bind("<Button-1>", lambda e: callback(site1))

if photo1!= -1:
    i1 = tk.Label(frame3, image=photo1)
    i1.pack(side=tk.TOP, fill=tk.BOTH)
    i1.bind("<Button-1>", lambda e: callback(map1))
else: tk.Label(frame3, text="no image retrieved").pack(side=tk.TOP, fill=tk.BOTH)

im2 = tk.Label(frame3, text=mon2.getName(), relief=tk.RIDGE, width=50, cursor="hand2")
im2.pack(side=tk.TOP, fill=tk.BOTH)
im2.bind("<Button-1>", lambda e: callback(site2))

if photo2!= -1:
    i2=tk.Label(frame3, image=photo2)
    i2.pack(side=tk.TOP, fill=tk.BOTH)
    i2.bind("<Button-1>", lambda e: callback(map2))
else:        tk.Label(frame3, text="no image retrieved").pack(side=tk.TOP, fill=tk.BOTH)


im3 = tk.Label(frame3, text=mon3.getName(), relief=tk.RIDGE, width=50,cursor="hand2")
im3.pack(side=tk.TOP, fill=tk.BOTH)
im3.bind("<Button-1>", lambda e: callback(site3))

if photo3!= -1:
    i3=tk.Label(frame3, image=photo3)
    i3.pack(side=tk.TOP, fill=tk.BOTH)
    i3.bind("<Button-1>", lambda e: callback(map3))
else:        tk.Label(frame3, text="no image retrieved").pack(side=tk.TOP, fill=tk.BOTH)

root.mainloop()




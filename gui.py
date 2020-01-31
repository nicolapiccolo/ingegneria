import tkinter as tk

root = tk.Tk()
root.geometry("1000x700")

frame1=tk.Frame(root, width=200,background="Blue")
frame1.pack(side=tk.LEFT, fill=tk.BOTH,expand=True)

frame2=tk.Frame(root, width=200,background="Green")
frame2.pack(side=tk.LEFT, fill=tk.BOTH,expand=True)

frame3=tk.Frame(root, width=200,background="Cyan")
frame3.pack(side=tk.LEFT, fill=tk.BOTH,expand=True)


label1 = tk.Label(frame2,text="ciao")
label1.pack(side=tk.TOP,fill=tk.BOTH,expand=True)

label2 = tk.Label(frame2,text="ciao1")
label2.pack(side=tk.TOP,fill=tk.BOTH,expand=True)

label3 = tk.Label(frame2,text="ciao2")
label3.pack(side=tk.TOP,fill=tk.BOTH,expand=True)


root.mainloop()





"""
master=tk.Tk()
master.geometry("1000x700")
master.update()

loaded_model = tf.keras.models.load_model('monumenti.h5')


frame1=tk.Frame(master, width=500, height=master.winfo_height(), background="Blue").pack(side=tk.LEFT, fill=tk.BOTH)

#frame1.grid(row=0, column=0, padx=10)


frame2=tk.Frame(master, width=200, height=master.winfo_height(), background="Green").pack(side=tk.LEFT, fill=tk.BOTH)

#frame2.grid(row=0, column=1, padx=10)

frame2_1 = tk.Frame(frame2, width=200, height=master.winfo_height()/2, background="Black").pack(side=tk.TOP, fill=tk.BOTH)

#grid(row=0, column=0)

frame2_2 = tk.Frame(frame2, width=200, height=master.winfo_height()/2, background="Grey").pack(side=tk.TOP, fill=tk.BOTH)
#grid(row=1, column=0)

frame3=tk.Frame(master, width=300, height=master.winfo_height(), background="Yellow").pack(side=tk.LEFT, fill=tk.BOTH)
#frame3.grid(row=0, column=2, padx=10)


path = filedialog.askopenfilename()
print(path)
photo = openImg(path)
tk.Label(frame1, image=photo).pack(side=tk.TOP, fill=tk.BOTH,expand=True)

monu = Dataset.getLabel(predict(path,loaded_model)[0])
monumento = Info(monu,'')

master.title("MonumentInfo: " + monu)


prop = getAllProps(monumento)
#prop = []

descr = tk.Label(frame2_1, text="prova", relief=tk.RIDGE, width=50).pack(side=tk.TOP,expand=True,fill=tk.BOTH)

r=0
for p in prop:
    if len(p[1])>0:
        tk.Label(frame2_2,text=p[0], relief=tk.RIDGE, width=20).pack(side=tk.TOP, fill=tk.BOTH)
        tk.Label(frame2_2,text=p[1], relief=tk.SUNKEN, width=35).pack(side=tk.TOP, fill=tk.BOTH)
    r=r+1


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


im1 = tk.Label(frame3, text=mon1.getName(), relief=tk.RIDGE, width=50, cursor="hand2").pack(side=tk.TOP, fill=tk.BOTH)
#im1.grid(row=0, column=0)
#im1.bind("<Button-1>", lambda e: callback(vicini[0]))

tk.Label(frame3, image=photo1).pack(side=tk.TOP, fill=tk.BOTH)

im2 = tk.Label(frame3, text=mon2.getName(), relief=tk.RIDGE, width=50, cursor="hand2").pack(side=tk.TOP, fill=tk.BOTH)
#im2.bind("<Button-1>", lambda e: callback(vicini[1]))

tk.Label(frame3, image=photo2).pack(side=tk.TOP, fill=tk.BOTH)
#.grid(row=3, column=0, pady=20)

im3 = tk.Label(frame3, text=mon3.getName(), relief=tk.RIDGE, width=50,cursor="hand2").pack(side=tk.TOP, fill=tk.BOTH)
#im3.grid(row=4, column=0)
#im3.bind("<Button-1>", lambda e: callback(vicini[2]))

tk.Label(frame3, image=photo3).pack(side=tk.TOP, fill=tk.BOTH)
#.grid(row=5, column=0, pady=20)


i=0
for v in vicini:
    photos = openImgURl()
    tk.Label(frame3, image=photos).grid(row=i, column=0)
    i = i+1


master.update()

#print(monu)
"""

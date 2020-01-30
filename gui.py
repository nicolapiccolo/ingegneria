from tkinter import *
from tkinter import filedialog
import PIL.ImageTk
from PIL import ImageTk


class Gui:
    def __init__(self,master):
        l_frame = Frame(master, width=500, height=400, bg='red').pack(side=LEFT)

        c_frame = Frame(master, width=200, height=400, bg='green').pack(side=LEFT)

        r_frame = Frame(master, width=200, height=400, bg='cyan').pack(side=LEFT)



        """
        img = PIL.Image.open(self.open())
        img = img.resize((250, 250), PIL.Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(img)
        imageView = Label(l_frame,image=photo).pack(side=LEFT)
        """



    def open(self):
        filename = filedialog.askopenfilename()
        if filename != "":
            return filename
        else:
            return -1



 img = ImageTk.PhotoImage(PIL.Image.open('monumenti/test/8.jpg'))
        panel = Label(master, image=img)
        panel.pack(side="bottom", fill="both", expand="yes")
root = Tk()
my_gui = Gui(root)


root.mainloop()


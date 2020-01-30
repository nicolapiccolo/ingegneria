from infoMonumento import Info
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


def openImgURl(url):
    img = PIL.Image.open(urlopen(url))
    img = img.resize((200, 150), PIL.Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(img)
    return photo

o = ['http://www.wikidata.org/entity/Q513023', 'http://www.wikidata.org/entity/Q550514', 'http://www.wikidata.org/entity/Q43332']

for p in o:
    photos = openImgURl(getImage(v))
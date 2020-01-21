from SPARQLWrapper import SPARQLWrapper, JSON
import pandas as pd

from infoMonumento import Info
from dataset import Dataset
from riconoscitore import Riconoscitore
from PIL import Image

import os
import tensorflow as tf
import numpy as np
import scipy as sci
import matplotlib.pyplot as plt
import matplotlib.image as mpim

from keras.models import load_model
from keras.preprocessing import image

data = Dataset('/Users/nicopiccolo/Desktop/monunosf',5,1)

r = Riconoscitore(data,15)
r.saveModel('monumenti.h5')

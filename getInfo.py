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

""""
query = "SELECT ?uri ?pp WHERE { ?uri rdfs:label 'colosseo'@it. ?uri wdt:P186 ?op. ?op rdfs:label ?pp  FILTER (lang(?pp)='it')}"

colosseo = Info("Colosseo")

colosseo.getAddress()
colosseo.getCulture()
colosseo.getMaterial()
colosseo.getStyle()
colosseo.getUse()
colosseo.getDataOpening()
colosseo.getVisitors()
"""


#results_df[['item.value', 'itemLabel.value']].head()

#for result in results["results"]["bindings"]:
 #   print(result["uri"]["value"] + "    " + result["pp"]["value"])
"""

sparqlwd = SPARQLWrapper("https://query.wikidata.org/sparql")
myid = "wd:Q22673982"
sparqlwd.setQuery(f"SELECT ?s ?p WHERE {{?s ?p {myid} .}}")
sparqlwd.setReturnFormat(JSON)
results = sparqlwd.query().convert()
print(results)
results_df = pd.io.json.json_normalize(results['results']['bindings'])
print(results_df)
"""

data = Dataset('/Users/nicopiccolo/Desktop/monunosf',5,1)


def loadImg(filename):
    np_image = Image.open(filename)
    new_image = np_image.resize((64, 64))
    np_image = np.array(new_image).astype('float32') / 255
    return np_image

def plotImages(images_arr):
    fig, axes = plt.subplots(1, 3, figsize=(5,5))
    axes = axes.flatten()
    for img, ax in zip(images_arr, axes):
        ax.imshow(img)
        ax.axis('off')
    plt.tight_layout()
    plt.show()
""""
img = loadImg('/Users/nicopiccolo/Desktop/monunosf/test/vittoriano/6.jpg')
#print(img)
imgplot = plt.imshow(img)
plt.show()
"""

loaded_model = tf.keras.models.load_model('monumenti.h5')
print(loaded_model.layers[0].input_shape) #(None, 160, 160, 3)

image_path="/Users/nicopiccolo/Desktop/proba/12.jpg"
img = image.load_img(image_path, target_size=(64, 64))
plt.imshow(img)
img = np.expand_dims(img, axis=0)
np_image = np.array(img).astype('float32') / 255
pred=loaded_model.predict_classes(np_image)
print(pred)
plt.show()



"""
monumento = Info()
monumento.getAddress()
monumento.getCulture()
monumento.getMaterial()

"""


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


loaded_model = tf.keras.models.load_model('monumenti.h5')
#print(loaded_model.layers[0].input_shape) #(None, 160, 160, 3)

image_path="monumenti/test/9.jpg"
img = image.load_img(image_path, target_size=(64, 64))
plt.imshow(img)
img = np.expand_dims(img, axis=0)
np_image = np.array(img).astype('float32') / 255
pred=loaded_model.predict_classes(np_image)
plt.show()

monu = Dataset.getLabel(pred[0])

#print(monu)

monumento = Info(monu)
print("Descrizione: " + monumento.getDescription())
print("Indirizzo: " + monumento.getAddress())
print("Cultura: " + monumento.getCulture())
print("Materiali usati: " + monumento.getMaterial())
print("Data apertura: " + monumento.getDataOpening())
print("Uso: " + monumento.getUse())
print("Stile: " + monumento.getStyle())
print("Visitatori annuali: " + monumento.getVisitors())
print("Architetto:" + monumento.getArchitect())
print("Epoca: " + monumento.getPeriod())
print("Religione: " + monumento.getReligion())
print("Diocesi: " + monumento.getDiocese())
print("Posizione: " + monumento.getPosition())
print("Nazione:" + monumento.getCountry())
print("Regione:" + monumento.getRegion())
print("Altezza:" + monumento.getHeight())
print("Larghezza:" + monumento.getWidth())
print("Sito Web:" + monumento.getWebsite())
print("Inizio:" + monumento.getStart())



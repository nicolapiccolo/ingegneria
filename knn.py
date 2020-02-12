import numpy as np
from SPARQLWrapper import SPARQLWrapper, JSON
import csv
import pandas as pd
import time
import urllib

from infoMonumento import Info

WD = "https://query.wikidata.org/sparql"
DB = "http://dbpedia.org/sparql"
DD = 'monuments.csv'

class Neighbors:
    dataset = ''

    def __init__(self):
        self.dataset = pd.read_csv(DD)

    def refreshCSV(self):
        query = """select ?uri ?lat ?lon
        where{
        ?uri wdt:P31 wd:Q570116.
        ?uri wdt:P17 ?p.
        ?uri wdt:P625 ?geo.
        FILTER (?p IN (wd:Q38,wd:Q237) )
        bind( replace( str(?geo), "^[^0-9\\\.]*([0-9\\\.]+) .*$", "$1" ) as ?lon )
        bind( replace( str(?geo), "^.* ([0-9\\\.]+)[^0-9\\\.]*$", "$1" ) as ?lat )
        }"""
        res = Info.setQuery(query,WD)
        self.writeCSV(res)



    def writeCSV(self,res):

        f = open('monuments.csv', 'w')
        with f:
            writer = csv.writer(f)
            writer.writerow(['LAT', 'LON', 'URI'])
            for result in res["results"]["bindings"]:
                lat = result["lat"]["value"]
                lon = result["lon"]["value"]
                uri = result["uri"]["value"]
                r = [lat, lon, uri]
                writer.writerow(r)


    def distance(self,instance1, instance2):
        # just in case, if the instances are lists or tuples:
        instance1 = np.array(instance1)
        instance2 = np.array(instance2)

        return np.linalg.norm(instance1 - instance2)



    def getImage(self,uri):
        query = f"SELECT ?img  WHERE {{ <{uri}> wdt:P18 ?img }}"
        res = Info.setQuery(query, WD)
        img = ''
        for result in  res["results"]["bindings"]:
            img = result['img']['value']
        print(img)
        return img


    def getAllUri(self,uri):
        tr = self.dataset.loc[self.dataset['URI']==uri]
        #print(tr)
        neighbors = self.get_neighbors(self.dataset, tr, 3, distance=self.distance)
        uris = []
        for n in neighbors:
            uris.append(n[0]['URI'].values[0])
        return uris


    def get_neighbors(self,training_set, test_instance, k, distance=distance):
        distances = []
        for index in range(len(training_set)):
            # if(training_set.loc[[index]]!=test_instance):
            train = training_set.loc[[index]]
            dist = self.distance(test_instance.iloc[:, 0:2], train.iloc[:, 0:2])
            if dist > 0: distances.append((training_set.loc[[index]], dist))
        distances.sort(key=lambda x: x[1])
        neighbors = distances[:k]
        return neighbors



import numpy as np
from SPARQLWrapper import SPARQLWrapper, JSON
import csv
import pandas as pd
import time
import urllib

WD = "https://query.wikidata.org/sparql"
DB = "http://dbpedia.org/sparql"
DD = 'monuments.csv'

class Neighbors:
    dataset = ''

    def __init__(self):
        self.dataset = pd.read_csv(DD)


    def setQuery(self,query, wrapper):
        sparql = SPARQLWrapper(wrapper)
        sparql.setQuery(query)
        sparql.setReturnFormat(JSON)
        while True:
            i = 1
            try:
                results = sparql.query().convert()
                return results["results"]["bindings"]
            except urllib.error.HTTPError:
                time.sleep(i)
                i += 1

    def writeCSV(self,res):

        f = open('monuments.csv', 'w')
        with f:
            writer = csv.writer(f)
            writer.writerow(['LAT', 'LON', 'URI'])
            for result in res:
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
        res = self.setQuery(query, WD)
        img = ''
        for result in res:
            img = result['img']['value']
        print(img)
        return img


    def getAllUri(self,uri):
        tr = self.dataset.loc[self.dataset['URI']==uri]
        print(tr)
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










query = """select ?uri ?lat ?lon
where{
?uri wdt:P31 wd:Q570116.
?uri wdt:P17 wd:Q38.
?uri wdt:P625 ?geo.
bind( replace( str(?geo), "^[^0-9\\\.]*([0-9\\\.]+) .*$", "$1" ) as ?lon )
bind( replace( str(?geo), "^.* ([0-9\\\.]+)[^0-9\\\.]*$", "$1" ) as ?lat )
}"""


#res = setQuery(query,WD)
#writeCSV(res)
#print (query)

#dataset = pd.read_csv('monuments.csv')

#tr = dataset.loc[dataset['URI'] == 'http://www.wikidata.org/entity/Q18068']
#rint(tr)
#x_train = dataset.drop('URI', axis=1)

#tr = dataset.loc[[2]]





#print(dataset[10])
#testset_data = iris_data[indices[-n_training_samples:]]
#testset_labels = iris_labels[indices[-n_training_samples:]]


#print(getImage(n[0]['URI'].values[0]))
#print(getImage(n[0]['URI'].values[0]))

#print(pp.values)
#print(get_neighbors(dataset,tr,3,distance=distance))






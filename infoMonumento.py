from SPARQLWrapper import SPARQLWrapper, JSON
import pandas as pd

WD = "https://query.wikidata.org/sparql"



class Info:

    instanceof = "P31"
    uri = ""
    def __init__(self, nome):
        self.nome = nome
        self.uri = self.getUri()


    def setQuery(self,query,wrapper):
        sparql = SPARQLWrapper(wrapper)
        sparql.setQuery(query)
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()
        return results

    def getUri(self):
        query = "SELECT ?uri " \
                "WHERE { " \
                "?uri rdfs:label '" + self.nome + "'@it. "\
                "?arc rdfs:label 'sito archeologico'@it. " \
                "?uri wdt:P31 ?arc" \
                "}"
        #print(query)
        results = self.setQuery(query,WD)
        for result in results["results"]["bindings"]:
            uri = result["uri"]["value"]
            print(uri)
        return uri

    def getAddress(self):
        query = f"SELECT ?cname ?addr  WHERE {{ <{self.uri}> wdt:P17 ?country. ?country rdfs:label ?cname. <{self.uri}> wdt:P6375 ?addr. FILTER(lang(?cname)='it') }}"
        #print(query)
        results = self.setQuery(query,WD)
        for result in results["results"]["bindings"]:
            addr = result["addr"]["value"] +" -- "+ result["cname"]["value"]
        print(addr)
        return addr

    def getCulture(self):
        query = f"SELECT ?name  WHERE {{ <{self.uri}> wdt:P2596 ?culture. ?culture rdfs:label ?name. FILTER(lang(?name)='it') }}"
        #print(query)
        results = self.setQuery(query, WD)
        for result in results["results"]["bindings"]:
            culture = result["name"]["value"]
        print(culture)
        return culture

    def getMaterial(self):
        query = f"SELECT ?name  WHERE {{ <{self.uri}> wdt:P186 ?material. ?material rdfs:label ?name. FILTER(lang(?name)='it') }}"
        #print(query)
        results = self.setQuery(query, WD)
        material = []
        for result in results["results"]["bindings"]:
            material.append(result["name"]["value"])
        print(material)
        return material


    def getStyle(self):
        query = f"SELECT ?name  WHERE {{ <{self.uri}> wdt:P149 ?style. ?style rdfs:label ?name. FILTER(lang(?name)='it') }}"
        #print(query)
        results = self.setQuery(query, WD)
        style = []
        for result in results["results"]["bindings"]:
            style.append(result["name"]["value"])
        print(style)
        return style

    def getDataOpening(self):
        query = f"SELECT ?data  WHERE {{ <{self.uri}> wdt:P1619 ?data }}"
        #print(query)
        results = self.setQuery(query, WD)
        dt = ""
        for result in results["results"]["bindings"]:
            dt = result["data"]["value"]
        print(dt)
        return dt

    def getVisitors(self):
        query = f"SELECT ?visit  WHERE {{ <{self.uri}> wdt:P1174 ?visit }}"
        #print(query)
        results = self.setQuery(query, WD)
        visitors = ""
        for result in results["results"]["bindings"]:
            visitors = result["visit"]["value"]
        print(visitors)
        return visitors

    def getUse(self):
        query = f"SELECT ?name  WHERE {{ <{self.uri}> wdt:P366 ?use. ?use rdfs:label ?name. FILTER(lang(?name)='it') }}"
        #print(query)
        results = self.setQuery(query, WD)
        use = []
        for result in results["results"]["bindings"]:
            use.append(result["name"]["value"])
        print(use)
        return use









from SPARQLWrapper import SPARQLWrapper, JSON
import pandas as pd

WD = "https://query.wikidata.org/sparql"
DB = "http://dbpedia.org/sparql"



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

    def getDescription(self):
        query = "SELECT ?o " \
                "WHERE { " \
                "?uri rdfs:label '" + self.nome + "'@it. " \
                "?uri dbo:abstract ?o " \
                "FILTER(lang(?o)='it')" \
                "}"
        # print(query)
        results = self.setQuery(query, DB)
        description = ''
        for result in results["results"]["bindings"]:
            description = result["o"]["value"]
        return description


    def getUri(self):
        query = "SELECT ?uri " \
                "WHERE { " \
                "?uri rdfs:label '" + self.nome + "'@it. "\
                "?arc rdfs:label 'tourist attraction'@en. " \
                "?uri wdt:P31 ?arc" \
                "}"
        #print(query)
        results = self.setQuery(query,WD)
        uri = ''
        for result in results["results"]["bindings"]:
            uri = result["uri"]["value"]
            #print(uri)
        return uri

    def getAddress(self):
        query = f"SELECT ?cname ?addr  WHERE {{ <{self.uri}> wdt:P17 ?country. ?country rdfs:label ?cname. <{self.uri}> wdt:P6375 ?addr. FILTER(lang(?cname)='it') }}"
        #print(query)
        results = self.setQuery(query,WD)
        addr = ''
        for result in results["results"]["bindings"]:
            addr = result["addr"]["value"] +" -- "+ result["cname"]["value"]
        #print(addr)
        return addr

    def getCulture(self):
        query = f"SELECT ?name  WHERE {{ <{self.uri}> wdt:P2596 ?culture. ?culture rdfs:label ?name. FILTER(lang(?name)='it') }}"
        #print(query)
        results = self.setQuery(query, WD)
        culture = ''
        for result in results["results"]["bindings"]:
            culture = result["name"]["value"]
        #print(culture)
        return culture

    def getMaterial(self):
        query = f"SELECT ?name  WHERE {{ <{self.uri}> wdt:P186 ?material. ?material rdfs:label ?name. FILTER(lang(?name)='it') }}"
        #print(query)
        results = self.setQuery(query, WD)
        material = ''
        for result in results["results"]["bindings"]:
            material += " " + result["name"]["value"]
        #print(material)
        return material


    def getStyle(self):
        query = f"SELECT ?name  WHERE {{ <{self.uri}> wdt:P149 ?style. ?style rdfs:label ?name. FILTER(lang(?name)='it') }}"
        #print(query)
        results = self.setQuery(query, WD)
        style = ''
        for result in results["results"]["bindings"]:
            style += " " + (result["name"]["value"])
        #print(style)
        return style

    def getDataOpening(self):
        query = f"SELECT ?data WHERE {{ <{self.uri}> wdt:P1619 ?data }}"
        #print(query)
        results = self.setQuery(query, WD)
        s = len(results["results"]["bindings"])
        if s<=0:
            query = f"SELECT ?data WHERE {{ <{self.uri}>  wdt:P517 ?data  }}"
            results = self.setQuery(query, WD)
        dt = ""
        for result in results["results"]["bindings"]:
            dt = result["data"]["value"]
        #print(dt)
        return dt

    def getVisitors(self):
        query = f"SELECT ?visit  WHERE {{ <{self.uri}> wdt:P1174 ?visit }}"
        #print(query)
        results = self.setQuery(query, WD)
        visitors = ""
        for result in results["results"]["bindings"]:
            visitors = result["visit"]["value"]
        #print(visitors)
        return visitors

    def getUse(self):
        query = f"SELECT ?name  WHERE {{ <{self.uri}> wdt:P366 ?use. ?use rdfs:label ?name. FILTER(lang(?name)='it') }}"
        #print(query)
        results = self.setQuery(query, WD)
        use = ''
        for result in results["results"]["bindings"]:
            use+= " " + (result["name"]["value"])
        #print(use)
        return use

    def getPeriod(self):
        query = f"SELECT ?name  WHERE {{ <{self.uri}> wdt:P2348 ?period. ?period rdfs:label ?name. FILTER(lang(?name)='it') }}"
        #print(query)
        results = self.setQuery(query, WD)
        period = ''
        for result in results["results"]["bindings"]:
            period+= " " + (result["name"]["value"])
        #print(use)
        return period

    def getReligion(self):
        query = f"SELECT ?name  WHERE {{ <{self.uri}> wdt:P140 ?religion. ?religion rdfs:label ?name. FILTER(lang(?name)='it') }}"
        #print(query)
        results = self.setQuery(query, WD)
        religion = ''
        for result in results["results"]["bindings"]:
            religion+= " " + (result["name"]["value"])
        #print(use)
        return religion

    def getDiocese(self):
        query = f"SELECT ?name  WHERE {{ <{self.uri}> wdt:P708 ?diocese. ?diocese rdfs:label ?name. FILTER(lang(?name)='it') }}"
        #print(query)
        results = self.setQuery(query, WD)
        diocese = ''
        for result in results["results"]["bindings"]:
            diocese+= " " + (result["name"]["value"])
        #print(use)
        return diocese

    def getPosition(self):
        query = f"SELECT ?name  WHERE {{ <{self.uri}> wdt:P276 ?position. ?position rdfs:label ?name. FILTER(lang(?name)='it') }}"
        #print(query)
        results = self.setQuery(query, WD)
        position = ''
        for result in results["results"]["bindings"]:
            position+= " " + (result["name"]["value"])
        #print(use)
        return position

    def getCountry(self):
        query = f"SELECT ?name  WHERE {{ <{self.uri}> wdt:P17 ?country. ?country rdfs:label ?name. FILTER(lang(?name)='it') }}"
        #print(query)
        results = self.setQuery(query, WD)
        country = ''
        for result in results["results"]["bindings"]:
            country+= " " + (result["name"]["value"])

        return country

    def getRegion(self):
        query = f"SELECT ?name  WHERE {{ <{self.uri}> wdt:P131 ?region. ?region rdfs:label ?name. FILTER(lang(?name)='it') }}"
        #print(query)
        results = self.setQuery(query, WD)
        region = ''
        for result in results["results"]["bindings"]:
            region+= " " + (result["name"]["value"])

        return region

    def getHeight(self):
        query = f"SELECT ?name  WHERE {{ <{self.uri}> wdt:P2048 ?height. ?height rdfs:label ?name. FILTER(lang(?name)='it') }}"
        #print(query)
        results = self.setQuery(query, WD)
        height = ''
        for result in results["results"]["bindings"]:
            height+= " " + (result["name"]["value"])

        return height

    def getWidth(self):
        query = f"SELECT ?name  WHERE {{ <{self.uri}> wdt:P2049 ?width. ?width rdfs:label ?name. FILTER(lang(?name)='it') }}"
        #print(query)
        results = self.setQuery(query, WD)
        width = ''
        for result in results["results"]["bindings"]:
            width+= " " + (result["name"]["value"])

        return width

    def getWebsite(self):
        query = f"SELECT ?name  WHERE {{ <{self.uri}> wdt:P856 ?website. ?website rdfs:label ?name. FILTER(lang(?name)='it') }}"
        #print(query)
        results = self.setQuery(query, WD)
        website = ''
        for result in results["results"]["bindings"]:
            website+= " " + (result["name"]["value"])

        return website

    def getArchitect(self):
        query = f"SELECT ?name  WHERE {{ <{self.uri}> wdt:P84 ?architect. ?architect rdfs:label ?name. FILTER(lang(?name)='it') }}"
        #print(query)
        results = self.setQuery(query, WD)
        architect = ''
        for result in results["results"]["bindings"]:
            architect+= " " + (result["name"]["value"])

        return architect

    def getStart(self):
        query = f"SELECT ?name  WHERE {{ <{self.uri}> wdt:P571 ?start. ?start rdfs:label ?name. FILTER(lang(?name)='it') }}"
        #print(query)
        results = self.setQuery(query, WD)
        start = ''
        for result in results["results"]["bindings"]:
            start+= " " + (result["name"]["value"])

        return start





from SPARQLWrapper import SPARQLWrapper, JSON
import urllib
import time

WD = "https://query.wikidata.org/sparql"
DB = "http://dbpedia.org/sparql"

import sys



class Info:

    instanceof = "P31"
    uri = ""
    nome = ""
    def __init__(self,nome,uri):
        if len(uri) < 1:
            self.nome = nome
            self.uri = self.getUri()
        else:
            self.nome = self.getName()
            self.uri = uri

    @classmethod
    def setQuery(cls, query, wrapper):

        user_agent = "MonumentInfo/%s.%s" % (sys.version_info[0], sys.version_info[1])
        sparql = SPARQLWrapper(wrapper,agent=user_agent)
        sparql.setQuery(query)
        sparql.setReturnFormat(JSON)
        while True:
            i = 1
            try:
                results = sparql.query().convert()
                return results
            except urllib.error.HTTPError as err:
                print(err)
                time.sleep(i)
                i += 1

    def getWiki(self):
        query = f"PREFIX foaf: <http://xmlns.com/foaf/0.1/> select ?descr where {{ ?uri owl:sameAs <{self.uri}>. ?uri foaf:isPrimaryTopicOf ?descr }} LIMIT 1"
        print(query)
        results = self.setQuery(query, DB)
        description = ''
        for result in results["results"]["bindings"]:
            description = result["descr"]["value"]
        return description

    def getDescription(self):
        query = f"select ?descr where {{ ?uri owl:sameAs <{self.uri}>. ?uri dbo:abstract ?descr. FILTER(lang(?descr)='it') }}"
        print(query)
        results = self.setQuery(query, DB)
        description = ''
        for result in results["results"]["bindings"]:
            description = result["descr"]["value"]
        return description


    def getUri(self):
        if len(self.uri)==0:
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
        else:
            return self.uri

    def getAddress(self):
        query = f"SELECT ?cname ?addr  WHERE {{ <{self.uri}> wdt:P17 ?country. ?country rdfs:label ?cname. <{self.uri}> wdt:P6375 ?addr. FILTER(lang(?cname)='it') }}"
        # print(query)
        results = self.setQuery(query, WD)
        addr = ''
        for result in results["results"]["bindings"]:
            addr = result["addr"]["value"] + " -- " + result["cname"]["value"]
        # print(addr)
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
            material += ", " + result["name"]["value"]
        #print(material)
        return material[1:]


    def getStyle(self):
        query = f"SELECT ?name  WHERE {{ <{self.uri}> wdt:P149 ?style. ?style rdfs:label ?name. FILTER(lang(?name)='it') }}"
        #print(query)
        results = self.setQuery(query, WD)
        style = ''
        for result in results["results"]["bindings"]:
            style += ", " + (result["name"]["value"])
        #print(style)
        return style[1:]

    def getDataOpening(self):
        query = f"SELECT ?d ?m ?y WHERE {{ <{self.uri}> wdt:P1619 ?data.  BIND (year(?data) AS ?y) BIND (month(?data) AS ?m) BIND (day(?data) AS ?d)}}"
        #print(query)
        results = self.setQuery(query, WD)
        s = len(results["results"]["bindings"])
        if s<=0:
            query = f"SELECT ?data WHERE {{ <{self.uri}>  wdt:P517 ?data  }}"
            results = self.setQuery(query, WD)
        dt = ""
        for result in results["results"]["bindings"]:
            dt = result["d"]["value"] + "/" + result["m"]["value"] + "/" + result["y"]["value"]
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
        i = len(visitors)
        v=i
        while v>0:
            if v!=i: visitors = visitors[:v] + "." + visitors[v:]
            v = v-3

        return visitors

    def getUse(self):
        query = f"SELECT ?name  WHERE {{ <{self.uri}> wdt:P366 ?use. ?use rdfs:label ?name. FILTER(lang(?name)='it') }}"
        #print(query)
        results = self.setQuery(query, WD)
        use = ''
        for result in results["results"]["bindings"]:
            use+= "," + (result["name"]["value"])
        #print(use)
        return use[1:]

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
            religion+= "," + (result["name"]["value"])
        #print(use)
        return religion[1:]

    def getDiocese(self):
        query = f"SELECT ?name  WHERE {{ <{self.uri}> wdt:P708 ?diocese. ?diocese rdfs:label ?name. FILTER(lang(?name)='it') }}"
        #print(query)
        results = self.setQuery(query, WD)
        diocese = ''
        for result in results["results"]["bindings"]:
            diocese = (result["name"]["value"])
        #print(use)
        return diocese

    def getPosition(self):
        query = f"SELECT ?name  WHERE {{ <{self.uri}> wdt:P276 ?position. ?position rdfs:label ?name. FILTER(lang(?name)='it') }}"
        #print(query)
        results = self.setQuery(query, WD)
        position = ''
        for result in results["results"]["bindings"]:
            position+= result["name"]["value"]
        #print(use)
        return position

    def getCountry(self):
        query = f"SELECT ?name  WHERE {{ <{self.uri}> wdt:P17 ?country. ?country rdfs:label ?name. FILTER(lang(?name)='it') }}"
        #print(query)
        results = self.setQuery(query, WD)
        country = ''
        for result in results["results"]["bindings"]:
            country= result["name"]["value"]

        return country

    def getRegion(self):
        query = f"SELECT ?name  WHERE {{ <{self.uri}> wdt:P131 ?region. ?region rdfs:label ?name. FILTER(lang(?name)='it') }}"
        #print(query)
        results = self.setQuery(query, WD)
        region = ''
        for result in results["results"]["bindings"]:
            region= result["name"]["value"]

        return region

    def getHeight(self):
        query = f"SELECT ?height  WHERE {{ <{self.uri}> wdt:P2048 ?height }}"
        print(query)
        results = self.setQuery(query, WD)
        height = ''
        for result in results["results"]["bindings"]:
            height= result["height"]["value"]

        return height

    def getWidth(self):
        query = f"SELECT ?width  WHERE {{ <{self.uri}> wdt:P2049 ?width }}"
        #print(query)
        results = self.setQuery(query, WD)
        width = ''
        for result in results["results"]["bindings"]:
            width= result["width"]["value"]

        return width

    def getWebsite(self):
        query = f"SELECT ?website  WHERE {{ <{self.uri}> wdt:P856 ?website }} LIMIT 1"
        #print(query)
        results = self.setQuery(query, WD)
        website = ''
        for result in results["results"]["bindings"]:
            website= result["website"]["value"]

        return website

    def getArchitect(self):
        query = f"SELECT ?name  WHERE {{ <{self.uri}> wdt:P84 ?architect. ?architect rdfs:label ?name. FILTER(lang(?name)='it') }}"
        #print(query)
        results = self.setQuery(query, WD)
        architect = ''
        for result in results["results"]["bindings"]:
            architect+= "\n- " + (result["name"]["value"])
        return architect[1:]

    def getGeolocation(self):
        q1 = """select ?lat ?lon
                where{ """

        q2=  """ wdt:P625 ?geo.
                bind( replace( str(?geo), "^[^0-9\\\.]*([0-9\\\.]+) .*$", "$1" ) as ?lon )
                bind( replace( str(?geo), "^.* ([0-9\\\.]+)[^0-9\\\.]*$", "$1" ) as ?lat )
                }"""
        query = q1 + "<"+ self.uri +">"+ q2
        print(query)
        results = self.setQuery(query, WD)
        loc = []
        for result in results["results"]["bindings"]:
            loc.append(result["lat"]["value"])
            loc.append(result["lon"]["value"])
        return loc

    def getName(self):
        if len(self.nome)==0:
            query=f"SELECT ?name WHERE {{<{self.uri}> rdfs:label ?name. FILTER(lang(?name)='it') }}"
            results = self.setQuery(query, WD)
            name = ''
            for result in results["results"]["bindings"]:
                name = result["name"]["value"]
                # print(uri)
            return name
        else:
            return self.nome







from SPARQLWrapper import SPARQLWrapper, JSON
import pandas as pd

from infoMonumento import Info

query = "SELECT ?uri ?pp WHERE { ?uri rdfs:label 'colosseo'@it. ?uri wdt:P186 ?op. ?op rdfs:label ?pp  FILTER (lang(?pp)='it')}"

colosseo = Info("Colosseo")

colosseo.getAddress()
colosseo.getCulture()
colosseo.getMaterial()
colosseo.getStyle()
colosseo.getUse()
colosseo.getDataOpening()
colosseo.getVisitors()


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
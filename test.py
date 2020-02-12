from infoMonumento import Info

monu='Colosseo'
m = Info('','http://www.wikidata.org/entity/Q10285')
print(m.getDescription())
print(m.getWiki())

geo1 = m.getGeolocation()
print(geo1)

map1=f"https://maps.google.com/maps?q={geo1[0]},{geo1[1]}&hl=es;z=14&amp;output=embed"
print(map1)
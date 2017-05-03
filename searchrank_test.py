from SearchRank.SearchRank import searchRank

#Parseamos el archivo con la información de los sitios
file = open("sites_db.dat")
sites_db = []
for line in file:
	(nom, desc, url, keywords_str, pond_str, auth_str) = line.split(",")
	keywords = keywords_str.split("|")
	pond = [float(i) for i in pond_str.split("|")]
	auth = int(auth_str)

	sites_db.append( (nom, desc, url, keywords, pond, auth) )

results = searchRank(sites_db, "fisica electromagnetismo", 1, 10)
print(results)
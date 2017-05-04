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

query_str = "fisica electromagnetismo"
print('Querying "'+query_str+'"...')
results = searchRank(sites_db, query_str, 1, 10)
for result in results:
	print(result)
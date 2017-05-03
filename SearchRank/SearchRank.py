from sys import stderr as stderr
import numpy as np
'''
Función searchRank: brinda los principales resultados para el usuario, en orden de relevancia

'''
def searchRank(sites_db, query, user_cat, num_results):
	#Sites_db es una lista de tuplas (for now) con los datos de los sitios web indexados
	results = []
	for (nombre, desc, url, keywords, pond, auth) in sites_db:
		if not auth: continue
		num_match = 0
		#Cuantas keywords de la query coinciden con las keywords del archivo?
		for word in (query.split" "):
			num_match += keywords.count(word)
		#Calculamos el ptje del archivo
		accuracy = num_match / len(keywords)
		file_score = accuracy * pond[user_cat]
		results.append( (file_score, nombre, desc, url) )

	return results


if __name__ == '__main__':
	print('Error: This function must be used as a module.', file=stderr)
import pickle

#dictionry saving and loading functions
def save_obj(obj, name ):
    with open('obj/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)
        print "SAVED TO",'obj/'+ name + '.pkl'

def load_obj(name ):
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)
        

artistDict = {}
try:
	artistDict = load_obj("artistDict")
	print "Dictionary Alread exists. Loaded."
except:
	print "Creating new dictionary."
	file = open("filteredPersons.idomaar")
	for line in file:
		try:
			splittedLine = line.split('\t')

			jsonData = splittedLine[3]
			artistObj = eval(jsonData)
			artistDict[ artistObj["name"] ] = splittedLine[1]
			print(artistObj["name"])
		except Exception as e:
			print(e)

	save_obj(artistDict,"artistDict")
	file.close()
	
print(len(artistDict.keys()))

file = open("similarArtists")
outFile = open("artist_artist","w")
for line in file:
	try:
		splittedLine = line.split('\t')
	
		artistName = splittedLine[0]
		artistId = artistDict[artistName]
		jsonData = splittedLine[1]
		simArtistObj = eval(jsonData)	

		simArtistList = [a["url"].split("/")[-1] for a in simArtistObj["similarartists"]["artist"]]
		simArtistsId = []
		for a in simArtistList:
			try:
				simArtistsId.append(artistDict[a])
			except:
				#print("Artist Not found")
				pass

		print(len(simArtistsId))
		outFile.write('\n'.join([ artistId+" "+a for a in simArtistsId ])+'\n')
		
	except Exception as e:
		print(e)

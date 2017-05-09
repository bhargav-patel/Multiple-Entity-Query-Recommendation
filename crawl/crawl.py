
f1 = open("../filteredDataset/fileteredArtists.idiomaar","r").readlines()

for line in f1:
	splits = line.split("\t")
	json = splits[3]
	data = eval(json)
	name = data["name"]
	

# -*- coding: utf-8 -*-

#	The goal of this project is to do some work on connected graphs
#	Question 0 is how to handle the data in a way that is efficient and convenient
#		Building an n*n graph with all n stations is probably extreme overkill so maybe the natural metro lines or a list of stations is best
#	Question 1, which seems fairly easy, is to get a short route from station A to station B
#		I think Breadth First Search is the way to go for that
#	Question 2, which seems very hard, is to determine how to transverse an entire metro grid
#		We'd need to figure out good starting points, good methods to choose where to go at each point and do a lot of computer work to get the list of trips

#	Let's start with some small lines to tackle 0 and 1
#	L1 Tetuán - Atocha Renfe
#	L2 Cuatro Caminos - Sevilla
#	L3 Moncloa - Lavapiés
#	L4 Argüelles - Alonso Martínez (this one will let us have some trips that require using three lines, which is nice to test things)
#	Update: lines are now long

L1 = ["Pinar de Chamartín", "Bambú", "Chamartín", "Plaza de Castilla", "Valdeacederas", "Tetuán", "Estrecho",
		"Alvarado", "Cuatro Caminos", "Ríos Rosas", "Iglesia", "Bilbao", "Tribunal", "Gran Vía", 
		"Sol", "Tirso de Molina", "Antón Martín", "Estación del Arte", "Atocha Renfe", "Menéndez Pelayo", 
		"Pacífico", "Puente de Vallecas", "Nueva Numancia", "Portazgo", "Alto del Arenal", "Miguel Hernández", 
		"Sierra de Guadalupe", "Villa de Vallecas", "Congosto", "La Gavía", "Las Suertes", "Valdecarros"]
L2 = ["Cuatro Caminos", "Canal", "Quevedo", "San Bernardo", "Noviciado", "Santo Domingo", "Ópera", "Sol",
		"Sevilla", "Banco de España", "Retiro", "Príncipe de Vergara", "Goya", "Manuel Becerra", "Ventas", 
		"La Elipa", "La Almudena", "Alsacia", "Avenida de Guadalajara", "Las Rosas"]
L3 = ["Moncloa", "Argüelles", "Ventura Rodríguez", "Plaza de España", "Callao", "Sol", "Lavapiés",
		"Embajadores", "Palos de la Frontera", "Delicias", "Legazpi", "Almendrales", 
		"Hospital 12 de Octubre", "San Fermín", "Ciudad de los Ángeles", 
		"Cruce de Villaverde", "San Cristóbal", "Villaverde Alto"]
L4 = ["Argüelles", "San Bernardo", "Bilbao", "Alonso Martínez", "Colón", "Serrano", "Velázquez", "Goya", 
		"Lista", "Diego de León", "Avenida de América", "Prosperidad", "Alfonso XIII", "Avenida de la Paz", 
		"Arturo Soria", "Esperanza", "Canillas", "Mar de Cristal", "San Lorenzo", "Parque de Santa María", 
		"Hortaleza", "Manoteras", "Pinar de Chamartín"]
L5 = ["Casa de Campo", "Campamento", "Empalme", "Aluche", "Eugenia de Montijo", "Carabanchel", "Vista Alegre", 
		"Oporto", "Urgel", "Marqués de Vadillo", "Pirámides", "Acacias", "Puerta de Toledo", "La Latina", 
		"Ópera", "Callao", "Gran Vía", "Chueca", "Alonso Martínez", "Rubén Darío", "Núñez de Balboa", 
		"Diego de León", "Ventas", "El Carmen", "Quintana", "Pueblo Nuevo", "Ciudad Lineal", "Suanzes", 
		"Torre Arias", "Canillejas", "El Capricho", "Alameda de Osuna"]
L6 = ["Moncloa", "Argüelles", "Príncipe Pío", "Puera del Ángel", "Alto de Extremadura", "Lucero", 
		"Laguna", "Carpetana", "Oporto", "Opañel", "Plaza Elíptica", "Usera", 
		"Legazpi", "Arganzuela-Planetario", "Méndez Álvaro", "Pacífico", "Conde de Casal", 
		"Sainz de Baranda",  "O'Donnell", "Manuel Becerra", "Diego de León", "Avenida de América", 
		"República Argentina", "Nuevos Ministerios", "Cuatro Caminos", "Guzmán el Bueno", 
		"Vicente Aleixandre", "Ciudad Universitaria", "Moncloa"]
L7 = ["Pitis", "Arroyofresno", "Lacoma", "Avenida de la Ilustración", "Peñagrande", "Antonio Machado",
		"Valdezarza", "Francos Rodríguez", "Guzmán el Bueno", "Islas Filipinas", "Canal", "Alonso Cano", 
		"Gregorio Marañón", "Avenida de América", "Cartagena", "Parque de las Avenidas", "Barrio de la Concepción", 
		"Pueblo Nuevo", "Ascao", "García Noblejas", "Simancas", "San Blas", "Las Musas", "Estadio Metropolitano", 
		"Barrio del Puerto", "Coslada Central", "La Rambla", "San Fernando", "Jarama", "Henares", "Hospital del Henares"]
FullMetro = [L1, L2, L3, L4, L5, L6, L7]

#	An important question now is: how do we know which stations are adjacent to a given one?
#	Making a list of stations and their neighbors seems reasonable, as we only have to "look" at the map once and then we have the data ready
#	Let's try:

connections = []
allStationsSimplelist = []

def isStationThere(station):
	for i,sublist in enumerate(connections):
		if sublist[0][0] == station:
			return i
	return -1


def makeConnections():
	for line in FullMetro:
		for station in line:
			if station not in allStationsSimplelist:
				allStationsSimplelist.append(station)
	for line in FullMetro:
		lastStationIndex = len(line) - 1
		for e,station in enumerate(line):
			#if not any(connections[0] == station for l in connections) # I think this is kinda cool but probably hard to read
			stationIndex = isStationThere(station)
			if stationIndex == -1:
				stationIndex = allStationsSimplelist.index(station)
				connections.append([(station, stationIndex)])
			else:
				stationIndex = allStationsSimplelist.index(station)
			if e > 0:
				for i,subtuple in enumerate(connections[stationIndex]):
					if subtuple[0] == line[e-1]:
						break
				else:
					connections[stationIndex].append((line[e-1], allStationsSimplelist.index(line[e-1])))
			if e < lastStationIndex:
				for i,subtuple in enumerate(connections[stationIndex]):
					if subtuple[0] == line[e+1]:
						break
				else:
					connections[stationIndex].append((line[e+1], allStationsSimplelist.index(line[e+1])))
				

			



import cProfile
#cProfile.run('makeConnections()')
makeConnections()

outputFile = open('Metro0.txt', 'w') #should we sort connections?
#connections.sort()
for i in connections: #export LC_CTYPE="es:ES.UTF-8" //that did something but not quite what I wanted
	for e in i[:-1]:
		outputFile.write(e[0] + ' | ')
	outputFile.write(i[-1][0] + '\n')

def connectTwoStations(station1, station2): #for now this will be gigaslow but let's just make it work
	bread = []		#for breadth lol
	trips = 0
	found = False
	bread.append([[station1]])
	foundStationsSimpleList = [station1]
	while not found:
		newTripLevel = []
		for previousList in bread[trips]:
			for previousStation in previousList:
				#print previousStation
				newDestinations = []
				for neighbor in connections[isStationThere(previousStation)][1:]:
					if neighbor not in foundStationsSimpleList:
						newDestinations.append(neighbor)
						foundStationsSimpleList.append(neighbor)
						#print connections[isStationThere(previousStation)]
						if neighbor == station2:
							print "Found!"
							previous2 = previousStation
							trip = []
							#while previous2 != station1:
							#	trip.append(previous2)
							newTripLevel.append(newDestinations)
							bread.append(newTripLevel)
							for asd in bread:
								print asd
							#print foundStationsSimpleList
							return True
				newTripLevel.append(newDestinations)
		bread.append(newTripLevel)
		trips += 1

def connectTwoStationsSecondWay(station1, station2):
	if isStationThere(station1) == -1 or isStationThere(station2) == -1:
		print "No conozco esa estación!"
		return False
	if station1 == station2:
		print "Un viaje rapitido"
		return 0
	bread = []
	trips = 0
	bread.append([(station1,0)])
	foundStationsSimpleList = [station1]
	while True:
		nextTripLevel = []
		for i,stationTuple in enumerate(bread[trips]):
			for neighbor in connections[isStationThere(stationTuple[0])][1:]:
				if neighbor not in foundStationsSimpleList:
					nextTripLevel.append((neighbor,i))
					foundStationsSimpleList.append(neighbor)
					if neighbor == station2:
						j = i
						toPrint = [neighbor]
						print "Puedes ir de " + station1 + ' a ' + station2 + " en " + str(trips + 1) + " viajes pasando por:"
						while trips > -1:
							city,j = bread[trips][j]
							trips -= 1
							toPrint.append(city)
						toPrint.reverse()
						for k,a in enumerate(toPrint):
							print str(k) + ": " + a
						return trips + 1
		bread.append(nextTripLevel)
		trips += 1


#cProfile.run('connectTwoStationsSecondWay("Casa de Campo", "Hospital del Henares")')

def longestFromStation(station):
	bread = []
	trips = 0
	totalStations = len(allStationsSimplelist)
	ogIndex = allStationsSimplelist.index(station)
	bread.append([ogIndex])
	foundStationsSimpleList = [0 for i in range(totalStations)] #this is very cool!! apparently very fast too
	foundStationsSimpleList[ogIndex] = 1
	foundStations = 1
	while True:
		#nextTripLevel = []
		#bread.append([])
		#for stationVisited in bread[trips]:
		nextTripLevel = {neighbor[1] for stationVisited in bread[trips] for neighbor in connections[stationVisited][1:] if foundStationsSimpleList[neighbor[1]] == 0} #set comprehension, cool
		#print nextTripLevel
		#print nextTripLevel
		#nextTripLevel2XD = [ele for ele in nextTripLevel if foundStationsSimpleList[ele] == 0]
		#print nextTripLevel2XD
		
		#nextTripLevel = set(nextTripLevel)
		#nextTripLevel = dict.fromkeys(nextTripLevel).keys()
		
		for ele in nextTripLevel:
			#if foundStationsSimpleList[ele] == 1:
				#foundStationsSimpleList.pop(ele)
				#continue
			#print ele
			foundStationsSimpleList[ele] = 1
			#print allStationsSimplelist[ele]
			#foundStations += 1
		foundStations += len(nextTripLevel)
			#print foundStations
		if foundStations >= totalStations:
			return allStationsSimplelist[list(nextTripLevel)[-1]], trips + 1
		#for neighbor in connections[stationVisited][1:]:	#neighbor is a (station, i) tuple
			#if neighbor[1] not in foundStationsSimpleList:
			#if foundStationsSimpleList[neighbor[1]] == 0:
				#nextTripLevel.append(neighbor[1])
				#bread[trips + 1].append(neighbor[1])
				#foundStationsSimpleList.append(neighbor[1])
				#foundStationsSimpleList[neighbor[1]] = 1
				#foundStations += 1
				#if foundStations == totalStations:
				#	return neighbor[0], trips + 1
		bread.append(nextTripLevel)
		#print bread
		trips += 1


#cProfile.run('longestFromStation("Casa de Campo")')

print longestFromStation("Casa de Campo")

def getLongestTripSLow(): #very slow
	maxTrips = 0
	for i1,c1 in enumerate(connections):
		for i2, c2 in enumerate(connections[i1 + 1:]):
			currentTrips = connectTwoStationsSecondWay(c1[0], c2[0])
			if maxTrips < currentTrips:
				maxTrips = currentTrips
				maxcities = (c1[0], c2[0])
	print maxTrips
	print maxcities[0] + ", " + maxcities[1]

def getLongestTripFast(): #fine but can be faster, slows down a lot with more stations added
	maxTrips = 0
	for c1 in connections:
		candidate = longestFromStation(c1[0])
		if candidate[1] > maxTrips:
			maxTrips = candidate[1]
			winnercities = (c1[0], candidate[0])
	print winnercities[0] + ", " + winnercities[1]
	print maxTrips									#this could still be improved a lot if we remember which stations we visited while making a long trip
													#because some of thsoe won't be candidates for a long trip anymore
	
def getLongestTripFastER():
	maxTrips = 0
	candidates = allStationsSimplelist[:]
	for neighList in connections:
		if len(neighList) == 2:
			oldStation = neighList[0][0]
			notCandidate = neighList[1][0]
			neighbors = connections[neighList[1][1]][1:]
			while len(neighbors) <= 3:
				candidates.pop(candidates.index(notCandidate))
				#print notCandidate
				for newNei in neighbors:
					if newNei[0] != oldStation:
						oldStation = notCandidate
						notCandidate = newNei[0]
						neighbors = connections[newNei[1]][1:]
						break
	#now with a reduced list of candidates we apply the bread
	#print candidates
	for c1 in candidates:
		candidate = longestFromStation(c1)
		if candidate[1] > maxTrips:
			maxTrips = candidate[1]
			winnercities = (c1, candidate[0])
	print "\n\033[0;32mLas estaciones que más lejos están son \033[0;36m" + winnercities[0] + "\033[0;32m y \033[0;36m" + winnercities[1] + "\033[0;32m, a \033[0;33m" + str(maxTrips) + "\033[0;32m paradas\033[0m\n"
	#print maxTrips
	#it seems slightly faster than the previous one but I believe it can still be optimized a lot



#cProfile.run('getLongestTripSlow()')

#print longestFromStation("Casa de Campo")

#cProfile.run('getLongestTripFast()')

cProfile.run('getLongestTripFastER()')

#major update: "isStationThere" is taking a lot of computing space when it's basically a function to get indexes
#we're just going to store stations as tuples so they have their index next to themselves, ready to be accessed
# done! this has increased setup time a bit maybe (<0.001 anyway), but time to get the longest trip is almost halved
# sub 0.05 now for L7 with the latest optimizations - but I believe it can still be A LOT better
# also, many functions in the program are probably broken now since I changed connections' structure

#LETSGOO the last changes made the function take a quarter of the time it was taking before !?!?
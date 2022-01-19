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

L1 = ["Pinar de Chamartín", "Bambú", "Chamartín", "Plaza de Castilla", "Valdeacederas", 
 		"Tetuán", "Estrecho", "Alvarado", "Cuatro Caminos", "Ríos Rosas", "Iglesia", "Bilbao", "Tribunal", 
		"Gran Vía", "Sol", "Tirso de Molina", "Antón Martín", "Estación del Arte", "Atocha Renfe"]
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
FullMetro = [L1, L2, L3, L4, L5, L6]

#	An important question now is: how do we know which stations are adjacent to a given one?
#	Making a list of stations and their neighbors seems reasonable, as we only have to "look" at the map once and then we have the data ready
#	Let's try:

connections = []

def isStationThere(station):
	for i,sublist in enumerate(connections):
		if sublist[0] == station:
			return i
	return -1


def makeConnections():
	for line in FullMetro:
		lastStationIndex = len(line) - 1
		for e,station in enumerate(line):
			#if not any(connections[0] == station for l in connections) # I think this is kinda cool but probably hard to read
			stationIndex = isStationThere(station)
			if stationIndex == -1:
				connections.append([station])
			if e > 0  and line[e-1] not in connections[stationIndex]:
				connections[stationIndex].append(line[e-1])
			if e < lastStationIndex and line[e+1] not in connections[stationIndex]:
				connections[stationIndex].append(line[e+1])
				

			



import cProfile
cProfile.run('makeConnections()')

outputFile = open('Metro0.txt', 'w') #should we sort connections?
for i in connections: #export LC_CTYPE="es:ES.UTF-8" //that did something but not quite what I wanted
	for e in i[:-1]:
		outputFile.write(e + ' | ')
	outputFile.write(i[-1] + '\n')

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
						#j = i
						#toPrint = [neighbor]
						#print "Puedes ir de " + station1 + ' a ' + station2 + " en " + str(trips + 1) + " viajes pasando por:"
						#while trips > -1:
						#	city,j = bread[trips][j]
						#	trips -= 1
						#	toPrint.append(city)
						#toPrint.reverse()
						#for k,a in enumerate(toPrint):
						#	print str(k) + ": " + a
						return trips + 1
		bread.append(nextTripLevel)
		trips += 1




#cProfile.run('connectTwoStationsSecondWay("Casa de Campo", "Parque de Santa María")')

def longestFromStation(station):
	#if isStationThere(station) == -1:
	#	print "No conozco esa estación!"
	#	return False
	bread = []
	trips = 0
	bread.append([station])
	foundStationsSimpleList = [station]
	foundStations = 1
	totalStations = len(connections)
	while True:
		nextTripLevel = []
		for stationVisited in bread[trips]:
			for neighbor in connections[isStationThere(stationVisited)][1:]:
				if neighbor not in foundStationsSimpleList:
					nextTripLevel.append((neighbor))
					foundStationsSimpleList.append(neighbor)
					foundStations += 1
					if foundStations == totalStations:
						return neighbor, trips +1
		bread.append(nextTripLevel)
		trips += 1


def getLongestTripSLow(): #1.something seconds
	maxTrips = 0
	for i1,c1 in enumerate(connections):
		for i2, c2 in enumerate(connections[i1 + 1:]):
			currentTrips = connectTwoStationsSecondWay(c1[0], c2[0])
			if maxTrips < currentTrips:
				maxTrips = currentTrips
				maxcities = (c1[0], c2[0])
	print maxTrips
	print maxcities[0] + ", " + maxcities[1]

def getLongestTripFast(): #0.063 seconds!
	maxTrips = 0
	for c1 in connections:
		candidate = longestFromStation(c1[0])
		if candidate[1] > maxTrips:
			maxTrips = candidate[1]
			winnercities = (c1[0], candidate[0])
	print winnercities[0] + ", " + winnercities[1]
	print maxTrips
		

#cProfile.run('getLongestTripSlow()')

#print longestFromStation("Casa de Campo")

cProfile.run('getLongestTripFast()')
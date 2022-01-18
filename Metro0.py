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

L1 = ["Tetuán", "Estrecho", "Alvarado", "Cuatro Caminos", "Ríos Rosas", "Iglesia", "Bibao", "Tribunal", 
		"Gran Vía", "Sol", "Tirso de Molina", "Antón Martín", "Estación del Arte", "Atocha Renfe"]
L2 = ["Cuatro Caminos", "Canal", "Quevedo", "San Bernardo", "Noviciado", "Santo Domingo", "Ópera", "Sol", "Sevilla"]
L3 = ["Moncloa", "Argüelles", "Ventura Rodríguez", "Plaza de España", "Callao", "Sol", "Lavapiés"]
L4 = ["Argüelles", "San Bernardo", "Bilbao", "Alonso Martínez"]
FullMetro = [L1, L2, L3, L4]

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
			if e > 0:
				connections[stationIndex].append(line[e-1])
			if e < lastStationIndex:
				connections[stationIndex].append(line[e+1]) #not handling repeats (lie l1 and l10 doing chamartín - plaza de castilla) atm, may not be worth it
				

			



import cProfile
cProfile.run('makeConnections()')

outputFile = open('Metro0.txt', 'w')
for i in connections: #export LC_CTYPE="es:ES.UTF-8" //that did something but not quite what I wanted
	for e in i[:-1]:
		outputFile.write(e + ' | ')
	outputFile.write(i[-1] + '\n')
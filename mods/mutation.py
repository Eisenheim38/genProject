import random
#muta algunos individuos de la poblacion
#poblacion=lista cromosomas, pm=probabilidad de mutacion de preferencia un valor entre 0.1-0.01
def mutar(poblacion,pm):
	for cromosoma in poblacion:
		if ( random.random()<= pm ): #por cada individuo se chequea si existe la probabilidad de que mute
			gen=random.randint(0,len(cromosoma)-1) #el gen que muta es seleccionado aleatoriamente
			alelos=range(0,4) #posibles alelos a mutar (posiciones de la fila(gen))
			for x in range(1,random.randint(2,4)):	#la cantidad de alelos a mutar es aleatoria
				mut=random.choice(alelos) #se escoge cual alelo mutar aleatoriamente
				alelos.remove(mut); #se extrae dicho alelo para no ser seleccionado en caso de que se mute mas de uno
				l_alelo=range(0,4)
				l_alelo.remove(cromosoma[gen][mut]) # el valor debe ser cualquier excepto el actual
				cromosoma[gen][mut]=random.choice(l_alelo)# se muta finalmente
	return poblacion


	
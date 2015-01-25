import random

#modulo de cruce, recibe poblacion retorna cruce de poblacion
#poblacion= individuos a cruzar , pc=probabilidad de cruce preferiblemente 0.7
def cruce(poblacion,pc): 
	nueva_poblacion=[[[]]]
	while (len(poblacion)>0):
		if len(poblacion)==1: #solo queda un individuo no es posible cruzarlo
			nueva_poblacion.append(poblacion[0])
		else:
		 	pareja1=poblacion[random.randint(0,len(poblacion)-1)] #seleccionamos la pareja 1 aleatoriamente
		 	poblacion.remove(pareja1);								#ya este individuo esta fuera de nuestra poblacion de cruce
			pareja2=poblacion[random.randint(0,len(poblacion)-1)] #seleccionamos la pareja 2 aleatoriamente
			poblacion.remove(pareja2);								#ya este individuo esta fuera de nuestra poblacion de cruce
			if random.random() <= pc: #se calcula la probabilidad de cruce
				a=len(pareja1)
				n=a/2
				np1=pareja1[0:n]+pareja2[n:a]
				np2=pareja2[0:n]+pareja1[n:a]   #se da cruce
				nueva_poblacion.append(np1)
				nueva_poblacion.append(np2)
			else:
				nueva_poblacion.append(pareja1)  # no hay cruce se clonan los individuos
				nueva_poblacion.append(pareja2)  
	return nueva_poblacion #se ha creado una nueva poblacion 
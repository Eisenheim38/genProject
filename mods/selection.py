def apt_gen_aprox(gen,w,zt):
	wf=(w-4)/2
	z=zt[i]*8 #vida zombie total
	p=gen.count(3)#potato-mine
	r=gen.count(2)#repeater
	n=gen.count(1)#peashooter
	damage=((r*2)+n)*wf+(p*8)
	zombie_survivors=damage-z
	return zombie_survivors

def apt_simul_aprox(gen,w,zt):
	z=zt[i]*8 #vida zombie total
	p=gen.count(3)#potato-mine
	r=gen.count(2)#repeater
	n=gen.count(1)#peashooter
	seed_damage=n+(r*2)
	for i in xrange(0,w-4):
		zombie_survivors=zombie_survivors-seed_damage
	if (zombie_survivors > 0):
		zombie_survivors=zombie_survivors-(seed_damage+(p*8))					
	return zombie_survivors # si el resultado es negativo el gen se adapta mejor

def puntuar(poblacion,w,zt):
	lp=len(poblacion[0])
	max_p=lp*w+0.0
	points=0
	puntuaciones=[]
	for x in range(len(poblacion)):
		for i in range(lp):
			points=simul(poblacion[x][i],w,zt,i+1)+points
		puntuaciones.append([points/max_p,x])
		points=0
	return sorted(puntuaciones,reverse=True)
	
def seleccionar(poblacion,puntuaciones):
	size = len(poblacion)/2
	minimo = 0.5
	maximo = 1.5
	n = 1
	ranking = []
	aux = puntuaciones[0][0]    #esta es la puntuacion del primer individuo
	for par in puntuaciones:
		ranking.append([n,par[1]])
		if aux != par[0]:
			n = n+1
		#print par[1],n
		aux = par[0]
	#print n
	i = 1
	for p in ranking:
		if p[0] == 1:
			#el caso en el que el ranking sea el menor
			t = minimo
		else:
			t = (1.0/p[0])*(minimo + (((maximo-minimo)*(i-1))/(p[0]-1)))
		p[0] = t
		i=i+1
	ranking = sorted(ranking,reverse=True)
	#print ranking
	nueva_poblacion = []
	for i in range(size):
		#print ranking[i][1]
		nueva_poblacion.append(poblacion[ranking[i][1]])
	#print nueva_poblacion
	return nueva_poblacion

def simul(gen,w,zt,i):
	z=zt[i]*8 #vida zombie total
	p=gen.count(3)#potato-mine
	r=gen.count(2)#repeater
	n=gen.count(1)#peashooter
	seed_damage=n+(r*2)
	hp_zombiea=8
	pos_actual=1
	while (z>0 and pos_actual<w):
		if pos_actual>w-4: #llegamos al jardin
			if gen[w-pos_actual]!= 3: #si la posicion no es de una papa
				seed_damage=seed_damage-gen[w-pos_actual] #la planta es eliminada por lo que las semillas no hace el mismos dano
			else: #es una papa
				if  hp_zombiea !=8 : #si es un zombie herido 
					z=z- hp_zombiea # lo termino de eliminar
				else:
					z=z-8 #elimino el zombie totalmente
				hp_zombiea=0 #zombie muerto 

		if(hp_zombiea >0):
			z=z-seed_damage
			hp_zombiea=hp_zombiea-seed_damage
		
		if(hp_zombiea<0):
			hp_zombiea=8+(hp_zombiea)	#murio zombie otro toma su lugar y recibe el dano sobrante
		elif(hp_zombiea==0):
			hp_zombiea=8 	#murio un zombie otro toma su lugar el siguiente turno en esta misma casilla por lo que no hay avence en pos_actual
		else:
			pos_actual=pos_actual+1 #un zombie cubre al siguiente por lo tanto pueden avanza

	return w-(pos_actual-1) # numero que representa que tan cerca llegaron los zombies 0 peor situacion w la mejor
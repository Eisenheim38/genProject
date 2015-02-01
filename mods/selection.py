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
	max_p=lp*w
	points=0
	puntuaciones=[[]]
	for x in range(0,len(poblacion)):
		for i in range(0,lp):
			points=simul(poblacion[x][i],w,zt)+points
		puntuaciones.append([points/max_p,x])
		points=0
	puntuaciones.sort()
	return puntuaciones

def seleccionar(poblacion,puntuaciones):
	return poblacion

def simul(gen,w,zt):
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
		if gen[w-pos_actual]!=3: #si la papa no ha matado al zombie , las semilla hacen su efecto
			z=z-seed_damage
			hp_zombiea=hp_zombiea-seed_damage
		if(hp_zombiea<0):
			hp_zombiea=8+(hp_zombiea)	#murio zombie otro toma su lugar y recibe el dano sobrante
		elif(hp_zombiea==0):
			hp_zombiea=8 	#murio un zombie otro toma su lugar el siguiente turno en esta misma casilla por lo que no hay avence en pos_actual
		else:
			pos_actual=pos_actual+1 #un zombie cubre al siguiente por lo tanto pueden avanza

	return w-pos_actual # numero que representa que tan cerca llegaron los zombies 0 peor situacion w la mejor
	



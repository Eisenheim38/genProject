def apt_gen_aprox(cromosoma,w,zt):
	wf=(w-4)/2
	z=zt[i]*8 #vida zombie total
	p=cromosoma.count(3)#potato-mine
	r=cromosoma.count(2)#repeater
	n=cromosoma.count(1)#peashooter
	damage=((r*2)+n)*wf+(p*8)
	zombie_survivors=damage-z
	return zombie_survivors

def apt_simul_aprox(cromosoma,w,zt):
	z=zt[i]*8 #vida zombie total
	p=cromosoma.count(3)#potato-mine
	r=cromosoma.count(2)#repeater
	n=cromosoma.count(1)#peashooter
	seed_damage=n+(r*2)
	for i in xrange(0,w-4):
		zombie_survivors=zombie_survivors-seed_damage
	if (zombie_survivors > 0):
		zombie_survivors=zombie_survivors-(seed_damage+(p*8))					
	return zombie_survivors # si el resultado es negativo el gen se adapta mejor

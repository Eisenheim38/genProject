def apt_gen(cromosoma,w,h,zt):
	wf=(w-4)/2
	z=zt[i]*4 #vida zombie total
	p=cromosoma.count(3)#potato-mine
	r=cromosoma.count(2)#repeater
	n=cromosoma.count(1)#peashooter
	damage=((r*2)+n)*wf
	zombie_survivors=damage-z
	dz=zombie_survivors+(p*4)#no deberia ser -(p*4)?
	return dz

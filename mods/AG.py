from selection import *
from mutation import *
from cross import *
import random

class Proy:
  """The place where the magic is."""
  #Class variables
  cromosomas = []
  zombies = []
  width = 0
  height = 0
  tam = 0

  #Class initializer
  #needs int w, int h, list of int z
  def __init__(self,w,h,z,zt):
    self.width = w
    self.height = h
    self.zombies = z
    self.zt = zt

  #Creates population
  def __init_population(self,t):
    for i in range(t):
      gen = []
      for j in range(self.height):
        gen.append([random.randint(0,3) for i in range(4)])
      self.cromosomas.append(gen)

  def cruce(self,poblacion,pc): 
    nueva_poblacion=[]
    while (len(poblacion)>0):
      if len(poblacion)==1: #solo queda un individuo no es posible cruzarlo
        nueva_poblacion.append(poblacion[0])
      else:
        pareja1=poblacion[random.randint(0,len(poblacion)-1)] #seleccionamos la pareja 1 aleatoriamente
        poblacion.remove(pareja1);                #ya este individuo esta fuera de nuestra poblacion de cruce
        pareja2=poblacion[random.randint(0,len(poblacion)-1)] #seleccionamos la pareja 2 aleatoriamente
        poblacion.remove(pareja2);                #ya este individuo esta fuera de nuestra poblacion de cruce
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

  def simulate(self,t):
    self.__init_population(t)
    i=0
    indice = 0 #Debe ser sustituido por el indice max de las puntuaciones
    solucion = False
    solucion_deseada = 1.0   #numero en el que la solucion es perfecta
    max_iter = 1000
    while (not solucion) and i!=max_iter:
      puntuaciones = puntuar(self.cromosomas,self.width,self.zt)
      #print puntuaciones
      for p in puntuaciones:
        if p[0] == solucion_deseada:
          solucion = True
          #print "Lo encontre!"
          indice = p[1]
          break
      seleccionados = seleccionar(self.cromosomas,puntuaciones) #esto deberia ser una lista con la mitad de la poblacion de mejor puntuacion
      cruzados = cruce(seleccionados,0.7)
      cruzados = mutar(cruzados,0.1)
      self.cromosomas = seleccionados + cruzados
      i = i+1
    if i == max_iter:
      #print max(puntuaciones)
      indice = max(puntuaciones)[1]
    #print "indice :"+str(i)
    #print puntuaciones
    for gen in self.cromosomas[indice]:
      print gen[0],gen[1],gen[2],gen[3] 
    #print self.cromosomas[indice]
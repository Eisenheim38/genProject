from selection import *
from mutation import *
#from cross import *
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
  def __init__(self,w,h,z):
    self.width=w
    self.height=h
    self.zombies=z

  #Creates population
  def __initPopulation(self,t):
    for i in range(t):
      gen = []
      for j in range(self.height):
        gen.append([random.randint(0,3) for i in range(4)])
      self.cromosomas.append(gen)

  def cruce(self,pc): 
    nueva_poblacion=[]
    while (len(self.cromosomas)>0):
      if len(self.cromosomas)==1: #solo queda un individuo no es posible cruzarlo
        nueva_poblacion.append(self.cromosomas[0])
      else:
        pareja1=self.cromosomas[random.randint(0,len(self.cromosomas)-1)] #seleccionamos la pareja 1 aleatoriamente
        self.cromosomas.remove(pareja1);                #ya este individuo esta fuera de nuestra poblacion de cruce
        pareja2=self.cromosomas[random.randint(0,len(self.cromosomas)-1)] #seleccionamos la pareja 2 aleatoriamente
        self.cromosomas.remove(pareja2);                #ya este individuo esta fuera de nuestra poblacion de cruce
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
    self.cromosomas = nueva_poblacion #se ha creado una nueva poblacion 

  def simulate(self,t):
    self.__initPopulation(t)
    for c in self.cromosomas:
      print c
    print 'After cross'
    self.cruce(0.7)
    for c in self.cromosomas:
      print c
    #print len(self.cromosomas)
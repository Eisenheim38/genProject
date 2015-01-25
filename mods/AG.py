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
  def __init__(self,w,h,z):
    self.width=w
    self.height=h
    self.zombies=z

  #Creates population
  def __initPopulation(self,t):
    for i in range(t):
      gen = []
      for j in range(4):
        gen.append([random.randint(0,3) for i in range(4)])
      self.cromosomas.append(gen)

  def simulate(self,t):
    self.__initPopulation(t)
    print self.cromosomas


		
from mods.AG import *
from sys import stdin

def main():
  """
  w = int(raw_input())
  h = int(raw_input())
  zi = int(raw_input())
  """
  whz = map(int,stdin.readline().split())
  zf = [0]*(whz[1]+1)
  z = map(int,stdin.readline().split())
  for i in z:
    zf[i] = zf[i]+1
  #p = Proy(10,1,[1,1,1])
  p = Proy(whz[0],whz[1],z)
  p.simulate(10)
 
if __name__=='__main__':
  main()
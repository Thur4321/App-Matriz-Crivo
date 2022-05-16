import numpy as np

numeros = None
matriz = None

class Matriz(object):

  def __init__(self, num):
    self.num = num

  def getNum(self):
    return self.num

  def matriz(self):
    global matriz 
    matriz = np.zeros((self.num, self.num))

  def crivo(self):
    global numeros
    numeros = [True]*(self.num*self.num)
    numeros[0] = False
    numeros[1] = False
    for i in range(2, self.num*self.num):
      if numeros[i]:
        for j in range(i*i,self.num*self.num,i):
           numeros[j]=False
    

  def matCrivo(self):
    global numeros
    global matriz
    mtCrivo = np.empty((self.num, self.num), dtype=str)
    n = 0
    for linha in range(0, self.num):
      for i in range(0, self.num):
        matriz[linha, i] = numeros[n]
        n += 1
    for i in range(0, self.num):
      for j in range(0, self.num):
        if matriz[i, j] == 1:
          mtCrivo[i, j] = 'T'
        else: 
          mtCrivo[i, j] = 'F'
    print(mtCrivo)
    
    
    
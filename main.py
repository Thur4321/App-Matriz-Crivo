from matriz import Matriz

class Main(object):

  num = int(input("Insira o tamanho da tabela: ")) 

  matriz = Matriz(num)

  matriz.matriz()
  matriz.crivo()
  matriz.matCrivo()
class Conjunto:
    def __init__(self):
        self.__conjunto=set()
    def Agregar(self):
        continuar=input('Ingresar elemento? S para continuar, N para concluir')
        while (continuar!='N'):
            self.elemento = int(input('Ingresar elemento'))
            self.__conjunto.add(self.elemento)
            continuar = input('Ingresar elemento? S para continuar, N para concluir')
    def Ordenar(self):
        return sorted(self.__conjunto)
    def getConjunto(self):
        return self.__conjunto
    def __add__(self, conjunto2):
        return self.__conjunto.union(conjunto2.getConjunto())
    def __sub__(self, conjunto2):
        return self.__conjunto.difference(conjunto2.getConjunto())
    def __eq__(self, conjunto2):
        return self.__conjunto==conjunto2.getConjunto()



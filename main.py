from claseConjunto import *

if __name__ == '__main__':
    opcion=None
    print("Ingresar conjuntos:")
    print("Conjunto 1:")
    conjunto1 = Conjunto().Agregar()
    print("Conjunto 2:")
    conjunto2 = Conjunto().Agregar()
    while(opcion!=0):
        opcion=input('''....Menu...
                     '0).Concluir'
                     '1).Unir los conjuntos'
                     '2).Restar los conjuntos'
                     '3).Verificar igualdad de 2 conjuntos'
                     ''')
        if opcion== '1':
            print("El conjunto resultante es: ",conjunto1+conjunto2)
        elif opcion=='2':
            print("El conjunto resultante es:",conjunto1-conjunto2)
        elif opcion=='3':
            resultado=(conjunto1==conjunto2)
            if resultado==True:
                print("Los conjuntos son iguales")
            else:
                print("Los conjuntos son diferentes")
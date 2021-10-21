def ultimos_tres_elementos(lista):
    listaa = lista[-3:]
    print(listaa)
ultimos_tres_elementos([1,3,4,5,2,76,3,1])

def ultimos_tres_elementos_concatenados(lista):
    print(lista[0][:-4:-1] + lista[1][:-4:-1] + lista[2][:-4:-1]) 

ultimos_tres_elementos_concatenados([[1,2,3,4], [5,6,7,8], [9,10,11,12]])

def indices_pares(lista):
    print(lista[::2])
indices_pares(["a","b","c","d","e"])

def indices_pares(lista):
    print(lista[1::2])
indices_pares(["a","b","c","d","e"])

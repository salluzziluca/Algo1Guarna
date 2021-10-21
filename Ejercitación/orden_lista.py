def ordenar_lista_menor_a_mayor(lista):
    lista_ordenada = lista.sort()
    return lista_ordenada
    
    

def ordenar_lista_mayor_a_menor(lista):
    lista.sort(reverse = True)
    print(lista)

ordenar_lista_mayor_a_menor([5,2,6,23,4]) 
    
    

def ordenar_lista_alfabeticamente(lista):
    lista_ordenada = lista.sort()
    return lista_ordenada
    

def ordenar_palabras_por_longitud(lista):
    def item_len(item):
        return len(item)
    lista_ordenada = lista.sort(key = item_len)
    return lista_ordenada
    
    
def ordenar_lista_por_tupla(lista):
    def segundo_valor(tupla):
        return tupla[1]
    lista_ordenada = lista.sort(key=segundo_valor)
    return lista_ordenada 
    

def ordenar_lista_por_suma_tupla(lista):
    def suma_valores(tupla):
        return (tupla[0] + tupla[1])
    lista_ordenada = lista.sort(key=suma_valores)
    return lista_ordenada 
    
    
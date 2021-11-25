"""Escribir una función que reciba una cadena de caracteres y devuelva una tupla con la cantidad de letras mayúsculas y minúsculas. La primer posición en la tupla, corresponde a las letras mayúsculas; y la segunda posición, a las letras minúsculas. Debe tener en cuenta las vocales acentuadas.
NO PUEDE UTILIZAR para esta solución el método count.
Deberá comprobar el correcto funcionamiento, mediante los siguientes casos de prueba usando la librería doctest.

Para ("Hola, ¿qué tal?") debe devolver (1, 9)
Para ("HoLaChAu") debe devolver (4, 4)
Para ("") debe devolver (0, 0)
Para ("42910%(@!") debe devolver (0, 0)
Para ("429A10É%(@!") debe devolver (2, 0)
Para ("90em28ú") debe devolver (0,3)
Para ("A MÍ MI MAMÁ ME MIMA") debe devolver (15, 0)
Para ("hola q tal?!") debe devolver (0, 8)

"""
import doctest

def contador(cadena):
    """recibe un string, devuelve una tupla con la cantidad de mayúsculas y la cantidad de minúsculas.
    
    >>> contador("Hola, ¿qué tal?")
    (1, 9)
    >>> contador("HoLaChAu")
    (4, 4)
    >>> contador("")
    (0, 0)
    >>> contador("42910%(@!")
    (0, 0)
    >>> contador("429A10É%(@!")
    (2, 0)
    >>> contador("90em28ú")
    (0, 3)
    >>> contador("A MÍ MI MAMÁ ME MIMA")
    (15, 0)
    >>> contador("hola q tal?!")
    (0, 8)
    
    """
    mayusculas = 0
    minisculas = 0

    for caracter in cadena:
        if caracter.isupper():
            mayusculas += 1
        elif caracter.islower():
            minisculas += 1
            
    mayusc_y_mins = (mayusculas, minisculas)
    return mayusc_y_mins
print(doctest.testmod())
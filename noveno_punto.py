def promedio (lista:float):
    lista:float = lista
    suma : float = 0
    for i in range (len (lista)):
        suma = suma + lista[i]
    promedio : float = suma / len(lista)
    print (f"EL promedio es: {promedio}")

def ordenar_ascedente (lista:float)->list:
    lista.sort()
    return lista

def ordenar_descendente (lista:float)->list:
    lista.sort(reverse = True)
    return lista


def promedio_multiplicativo (lista:float)->float:
    producto : float = 1
    for i in range (len (lista)):
        producto *= lista[i]
    promedio : float = producto** (1/len(lista))
    print (f"EL promedio multiplicativo es: {promedio}")
    return promedio

def mediana (lista:float):
    lista = ordenar_descendente (lista)
    mediana : float = lista [2] 
    print (f"La mediana es: {mediana}")
    return mediana

def potencia (lista:float):
    lista = ordenar_descendente (lista)
    potencia : float = lista[0]**lista[4]
    print (f"La potencia es de {lista[0]} elevado a {lista[4] } es: {potencia}")
    return potencia

def raiz_cubica (lista:float):
    lista= ordenar_descendente (lista)
    raiz : float = lista[4]**(1/3)
    print (f"La raiz cúbica de {lista[4]} es: {raiz}")
    return raiz
    

if __name__ == "__main__":
    lista_numero : float = []
    for i in range (5):
        numero : float =  float (input (f"Ingrese el {i+1} numero: "))
        lista_numero.append (numero)
    print (lista_numero)
    promedio (lista_numero)
    mediana(lista_numero)
    promedio_multiplicativo(lista_numero)
    print (f"La lista ordenada de forma ascendente es: {ordenar_ascedente (lista_numero)}")
    print (f"La lista ordenada de forma descendente es: {ordenar_descendente(lista_numero)}")
    potencia(lista_numero)
    raiz_cubica(lista_numero)


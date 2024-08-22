
def contar (lista):
    for i in range (len (lista)):
        cadena = lista [i]
        for j in range (len (cadena)):
            cont = cadena.count ("a") + cadena.count ("e") + cadena.count ("i") + cadena.count ("o") + cadena.count ("u")   
        if (cont) > 2:
            print (cadena)
    if (cont < 2):
        print ("No existe")

if __name__ == "__main__":
    cantidad :int = int(input("Ingrese la cantidad de elementos que va a tener la lista: "))
    lista = []
    for i in range (cantidad):
        elemento = input(f"Ingrese el elemento {i+1}: ")
        lista.append (elemento)
    contar (lista)
    

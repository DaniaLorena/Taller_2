

def llenar_matriz (cantidad: int): #
    matriz : int =[]
    suma_base : int = 0
    h: int =0
    for i in range (cantidad):
        fila : int = []
        for j in range (cantidad):
            elemento: int = int(input(f"Ingrese el elemento de la fila {i+1} y columna {j+1}: "))
            suma_base += elemento
            fila.append(elemento)
        matriz.append (fila)
    suma_base = suma_base / cantidad
    return matriz, suma_base


def sumar_filas (matriz, suma_base):
    for fila in matriz:
        suma_fila: int = 0
        for elemento in fila:
            suma_fila += elemento
    if (suma_fila == suma_base):
        return suma_fila
    else:
        return (f"La suma es {suma_fila}")


def sumar_columnas (matriz, suma_base):
    for columna in range (len(matriz [0])):
        sumar_columna: int = 0
        for fila in matriz:
            sumar_columna += (fila[columna])
    if (sumar_columna == suma_base):
        return sumar_columna
    else:
        return (f"La suma es {sumar_columna}")
    
def sumar_diagonal (matriz, suma_base):
    diagonal : int = 0
    for i in range(len(matriz)):
        diagonal += matriz[i][i]

    if (diagonal == suma_base):
        return diagonal
    else:
        return (f"La suma es diferente a la suma base{diagonal}")
    
def comparar (matriz, suma_base):
    suma_fila = sumar_filas (matriz, suma_base)
    suma_columna = sumar_columnas (matriz, suma_base)
    suma_diagonal = sumar_diagonal (matriz, suma_base)
    if (suma_fila == suma_columna) and (suma_columna == suma_diagonal):
        print (f"LA MATRIZ ES MÁGICA")
        print (f"La suma base es: {suma_base}")
        for i in matriz:
            print (i, end= " ")
            print ()
    else: 
        print (f"LA NO MATRIZ ES MÁGICA")
        print (f"La suma base es: {suma_base}")
        for i in matriz:
            print (i, end= " ")
            print ()
    


if __name__ == "__main__":
    cantidad : int = int (input("Ingrese que dimension desea que tenga la matriz cuadrada: "))
    matriz, suma =  llenar_matriz (cantidad)
    comparar (matriz, suma)



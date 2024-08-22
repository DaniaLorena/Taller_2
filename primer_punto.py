def separar_digitos(numero:int)->int:
    #Si el numero es negativo se multiplica por menos 1 para obtener su valor positivo
    if numero < 0:
        numero *= -1

    # Calculamos el número de dígitos
    divisor = 1
    #Se crea un bucle while para saber que divisor es el indicado para obtener el primer digito
    while numero // divisor >= 10:
        divisor *= 10

    #Se crea otro bucle while para ir separando los digitos por orden
    while divisor > 0:
        #Se obtiene el primer digito
        digito : int = numero // divisor
        print(digito, end=" ")
        #Se actualiza el valor del numero por el modulo de la operacion
        numero = numero % divisor
        #En cada iteracion se va simplificando el divisor
        divisor : int = divisor // 10

if __name__ == "__main__":
    #Se pide el numero entero a usuario
    num :int = int (input("Ingrese un numero: "))
    #Se utiliza la funcion 
    separar_digitos(num)




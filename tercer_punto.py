'''Desarrollar un programa que permita ingresar dos números enteros y determinar si se tratan de números espejos, 
definiendo números espejos como dos números a y b tales que a se lee de izquierda a derecha igual que se lee b de derecha a izquierda, y viceversa.
'''
#Se crea una funcion que va a comparar los numeros
def determinar (num_1 : int, num_2 : int):
    numero : int = num_1
    suma =0
    #Se crea un bucle
    while num_1 > 0:
        #Separa el  ultimo digito y se multiplica x 10 la suma para obtener el reveso
        suma = num_1 % 10 + suma*10
        #se obtiene la parte decimal
        num_1 = num_1//10
    #Se comparan los numeros
    if (suma==num_2):
        print (f"Los numeros {numero} y {num_2} SON ESPEJO")
    else:
        print (f"Los numeros {numero} y {num_2} NO SON ESPEJO")


if __name__ == "__main__":
    #Se piden los numeros
    numero_1 = int(input("Ingrese el primer número entero: "))
    numero_2 = int(input("Ingrese el segundo número entero: "))
    determinar (numero_1, numero_2)


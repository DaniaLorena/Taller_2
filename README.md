# Taller_2
> #### Los MECAPRORES
> - Rafael David Martínez Ovallos
> - Dania Lorena Pérez Moreno
>
[![logo-grupo.png](https://i.postimg.cc/T1KTDnfG/logo-grupo.png)](https://postimg.cc/vxdRRg4S)
### Primer Punto
Desarrollar un programa que ingrese un número entero n y separe todos los digitos que componen el número. Pista: Utilice los operadores módulo (%) y división entera (//).
> Explicación:
>

```
def separar(numero):
    if numero < 0: #Si el numero es negativo se multiplica por menos 1 para obtener su valor positivo
        numero *= -1

    divisor = 1 # Calculamos el número de dígitos
    while numero // divisor >= 10: #Se crea un bucle while para saber que divisor es el indicado para obtener el primer digito
        divisor *= 10

    i : int = 0 #Se crea otro bucle while para ir separando los digitos por orden
    while divisor > 0:
        digito = numero // divisor  #Se obtiene el primer digito
        print(digito, end=" ")
        numero = numero % divisor  #Se actualiza el valor del numero por el modulo de la operacion
        divisor = divisor // 10 #En cada iteracion se va simplificando el divisor
        i+=1
    return digito, i

if __name__ == "__main__":
    numero : int = int(input("Ingresa un número entero: "))
    #Se llama a la funcion separar
    separar(numero)
```
### Segundo Punto
Desarrollar un programa que ingrese un número flotante n y separe su parte entera de la parte decimal, y luego entregue los dígitos tanto de la parte entera como de la decimal.
> Explicación:
> En el punto 2 se nos solicita que a un numero flotante separemos la parte entera de la parte decimal y entregemos sus digitos por separado.
>
>En este caso como recorrer un dato de tipo int o float es imposible primero se convierte en un dato de tipo string para que así se pueda recorrer digito por digito y almacenarlos en una lista.
```
numero : str = str(x) 
numero_separado = []  
for digito in numero: 
    numero_separado.append(digito) 
```
>Despues de haberlo almacenado en la lista se busca la posición donde se encuentra el punto decimal ya que como sabemos todo numero que se encuentre antes del punto decimal se sabe que es la parte entera mientras que si se encuentran despues por lo tanto es la parte decimal
>
```
 posicion_decimal : int = numero_separado.index(".") 
```
>Ya sabiendo la posición del punto decimal solo se debe recorrer la lista y en este caso utilizamos el Slicing para recorrerla de forma más eficiente.
```
La parte entera es {numero_separado[:posicion_decimal]} y la parte decimal es {numero_separado[posicion_decimal + 1:]}
```
##### Código:
```
# Punto 2
def separar_digitos(x : float):
    numero : str = str(x) # Convierte el número en String
    numero_separado = []  # Almacena los digitos separados 
    for digito in numero: # Recorre la cadena 
        numero_separado.append(digito) # Agrega los digitos en la lista
    posicion_decimal : int = numero_separado.index(".") # Identifica la posición del punto decimal
    return (f'La parte entera es {numero_separado[:posicion_decimal]} y la parte decimal es {numero_separado[posicion_decimal + 1:]}')

if __name__ == "__main__":
    numero : float = float(input("Digite un número: "))
    print(separar_digitos(numero))
```


### Tercer Punto
Desarrollar un programa que permita ingresar dos números enteros y determinar si se tratan de números espejos, definiendo números espejos como dos números a y b tales que a se lee de izquierda a derecha igual que se lee b de derecha a izquierda, y viceversa.
> Explicación:
> 

```
def determinar (num_1 : int, num_2 : int): #Se crea una funcion que va a comparar los numeros
    numero : int = num_1
    suma =0    
    while num_1 > 0: #Se crea un bucle      
        suma = num_1 % 10 + suma*10   #Separa el  ultimo digito y se multiplica x 10 la suma para obtener el reveso
        #se obtiene la parte decimal
        num_1 = num_1//10
    if (suma==num_2):  #Se comparan los numeros
        print (f"Los numeros {numero} y {num_2} SON ESPEJO")
    else:
        print (f"Los numeros {numero} y {num_2} NO SON ESPEJO")

if __name__ == "__main__":
    #Se piden los numeros
    numero_1 = int(input("Ingrese el primer número entero: "))
    numero_2 = int(input("Ingrese el segundo número entero: "))
    determinar (numero_1, numero_2)
```
### Cuarto Punto
Diseñar una función que permita calcular una aproximación de la función coseno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Taylor. nota: use math para traer la función coseno y mostrar la diferencia entre el valor real y la aproximación. Calcule con cuántos términos de la serie (i.e: cuáles valores de n), se tienen errores del 10%, 1%, 0.1% y 0.001%.
$$cos(x) =\sum_{n=0}^{\infty}(-1)^{n}\frac{x^{2n}}{(2n)!}$$
> Explicación:
> En el punto 4 se nos solicita que utilizando las series de taylor aproximemos el valor del coseno para un ángulo en radianes y despues determinar cuantos polinomios se necesitan para llegar a cierto porcentaje de desviación.
> Primero conociendo la función de Taylor del coseno que es:
$$cos(x) =\sum_{n=0}^{\infty}(-1)^{n}\frac{x^{2n}}{(2n)!}$$
> Escribimos una función en python que permita aproximar el valor del coseno utilizando un número limitado de terminos:
```
def coseno_aproximado(x: float, num_terminos: int):
    suma = 0
    for n in range(num_terminos): 
        termino = ((-1) ** n) * (x ** (2 * n)) / math.factorial(2 * n) 
        suma += termino
    return suma
```
> Ahora se evalua la función y dependiendo el resultado se van agregando terminos a al polinomio hasta que se acerque a un porcentaje de error seleccionado por el usuario:
```
desviacion : float = abs((coseno_aproximado(angulo,terminos)-COSENO)/COSENO)
    while desviacion > PORCENTAJE:
        terminos += 1
        desviacion = abs((coseno_aproximado(angulo,terminos)-COSENO)/COSENO)
```
> PDT: Inicialmente teniamos como condición en el ciclo while que desviacion < PORCENTAJE, tras pruebas nos dimos cuenta que la función no hacia ninguna iteración despues de cambios y cambios le preguntamos a ChatGpt el porque de esto y resulta que la desviación siempre va a ser mayor en el primer termino que mientras más se vallan agregando terminos a la función más se va a ir acercando al valor real es decir en el termino 2 tiene una desviación del 20% por ende para el termino 8 tiene que tener una desviación mucho menor al 20%.

##### Código:
```
# Punto 4
import math
angulo : float = float(input("Digite el valor del ángulo en radianes: ")) 
COSENO : float = math.cos(angulo)
PORCENTAJE : float = float(input("Digite el porcentaje de desviación: "))

def coseno_aproximado(x: float, num_terminos: int):
    suma = 0
    for n in range(num_terminos): 
        termino = ((-1) ** n) * (x ** (2 * n)) / math.factorial(2 * n) # Se evalua la serie de Taylor para aproximar el coseno
        suma += termino
    return suma

if __name__ == "__main__":
    terminos : int = 0
    desviacion : float = abs((coseno_aproximado(angulo,terminos)-COSENO)/COSENO)
    while desviacion > PORCENTAJE:
        terminos += 1
        desviacion = abs((coseno_aproximado(angulo,terminos)-COSENO)/COSENO)
    print(f'Para el valor del coseno del ángulo {angulo} en radianes se necesitan {terminos} terminos para una aproximación del {PORCENTAJE}%')
    print(f'El valor del coseno para el angulo {angulo} es {COSENO} y su aproximación es de {coseno_aproximado(angulo,terminos)}')
```
### Quinto Punto
Desarrollar un programa que permita determinar el Minimo Comun Multiplo de dos numeros enteros. Abordar el problema desde una perpectiva tanto iterativa como recursiva. Pista: Puede ser de utilidad chequear el Algoritmo de Euclides para el cálculo del Máximo Común Divisor, y revisar cómo se relaciona este último con el Mínimo Común Múltiplo.
> Explicación:
> 
```
def mcd (x_1, y_1):
    mod = x_1 % y_1
    mod_previo = mod
    while mod !=0:
        mod_previo = mod
        x_a = y_1
        y_a =mod 
        mod = x_a % y_a
        if (mod == 0):
            break
    return mod_previo

def mcm (x_1, y_1):
    max_comun_div = mcd (x_1, y_1)
    mcm = (x_1/ max_comun_div)*y_1 
    return mcm 

if __name__ == "__main__":
    num_1 :int = int(input("Ingrese el primer numero: "))
    num_2 :int = int(input("Ingrese el segundo numero: "))
    print (f"El maximo comun divisor de {num_1} y {num_2} es: {mcd (num_1, num_2)}")
    print (f"El minimo comun multiplo de {num_1} y {num_2} es: {mcm (num_1, num_2)}")

```
### Sexto Punto
Desarrollar un programa que determine si en una lista existen o no elementos repetidos. Pista: Maneje valores booleanos y utilice el operador in.
> Explicación:
> En el punto 6 se nos solicita que recorramos una lista para evaluar si algun elemento de la lista se repite.
Primero se crea una lista donde se van almacenando los elementos de la primera lista, entonces antes de agregar los elementos se evalua si alguno se repite por ende si alguno se repite ya la función nos devuelve como resultado un booleano
>
```
def repetidos (lista):
    elementos_no_repetidos = [] 
    for elementos in lista: 
        if elementos in elementos_no_repetidos: 
            return True
        elementos_no_repetidos.append(elementos)
    return False 
```
#### Código:
```
# Punto 6
def repetidos (lista):
    elementos_no_repetidos = [] # Lista vacia para tener registro de los elementos en nuestra lista
    for elementos in lista: # Permite recorrer la lista
        if elementos in elementos_no_repetidos: # Evalua si hay elementos repetidos
            return True
        elementos_no_repetidos.append(elementos)
    return False #Al recorrer la lista y no encontrar elementos repetidos retorna False

if __name__ == "__main__":
    elementos : int = int(input("Digite cuantos elementos tendra la lista: "))
    numeros = []
    for i in range(elementos):
        elemento : int = int(input("Digite un número: ")) 
        numeros.append(elemento)
    if repetidos(numeros): 
        print(f'La lista {numeros} tiene elementos repetidos')
    else:
        print(f'La lista {numeros} no tiene elementos repetidos')
```
### Séptimo Punto
Desarrollar un programa que determine si en una lista se encuentra una cadena de caracteres con dos o más vocales. Si la cadena existe debe imprimirla y si no existe debe imprimir 'No existe'.
> Explicación:
>
```
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
```

### Octavo Punto
Desarrollar un programa que dadas dos listas determine que elementos tiene la primer lista que no tenga la segunda lista. Ejemplo:
[![Captura-de-pantalla-2024-08-21-213144.png](https://i.postimg.cc/FHGSM9S2/Captura-de-pantalla-2024-08-21-213144.png)](https://postimg.cc/DSJms3Bg)
> Explicación:
>En el punto 8 se nos solicita comparar 2 litas y retornar los elementos que se encuentran en la primera lista y no se encuentran en la segunda.
Para eso creamos una tercera lista donde se almacenan los datos faltantes, para eso primero recorremos la primera lista y comparamos los elementos con la segunda lista, si los elementos no se encuentran en la 
segunda lista se van agregando a la tercera lista.
>
```
def complemento (lista1, lista2):
    lista3 = [] 
    for elemento in lista1: 
        if elemento not in lista2: está o no en la lista
            lista3.append(elemento) 
    return lista3
```
#### Código:
```
def complemento (lista1, lista2):
    lista3 = [] # Lista vacia donde se almacenan los elementos faltantes
    for elemento in lista1: # Recorre la lista
        if elemento not in lista2: # Evalua si un elemento está o no en la lista
            lista3.append(elemento) 
    return lista3

if __name__ == "__main__":
    Lista1 = []
    Lista2 = []
    elementos_lista1 : int = int(input("Digite cuantos elementos tendra la lista: ")) 
    elementos_lista2 : int = int(input("Digite cuantos elementos tendra la lista: ")) 
    elemento_lista1  = (input("Digite un elemento para la lista 1"))
    Lista1.append(elemento_lista1)
    for i in range(elementos_lista2):
        elemento_lista2  = (input("Digite un elemento para la lista 2"))
        Lista2.append(elemento_lista2)
    Lista3 = complemento(Lista1,Lista2)
    print(f'Los elementos faltantes en la Lista 2 son: {Lista3}')
```

### Noveno Punto
Resolver el punto 7 del taller 1 usando operaciones con vectores.
> Explicación:

### Décimo Punto
Resolver el punto 7 del taller 1 usando operaciones con vectores.
> Explicación:
> En el punto 10 se nos socilita que a los números de una lista tome aquellos números que son multiplos de 3 y los seleccione en otra lista.
Se nos pone como reto hacerlo sin utilizar el operador modulo (%), por lo que primero partimos del hecho de que un número siempre sera multiplo de 3 siempre y cuando la suma de sus digitos de multiplo de 3
###### Ejemplo:
$$936\rightarrow 9+3+6 = 18$$
> Como 18 es multiplo de 3 por ende 936 tambien es multiplo de 3 aunque ahora tenemos un limitante y es que tambien necesitamos saber si 18 es multiplo de 3 por lo que si aplicamos la misma operación obtenemos:
$$18\rightarrow 1+8 = 9$$
>Por lo que para hacerlo más sencillo alteraremos un poco la definición anteriormente planteada teniendo en cuenta que 3, 6 y 9 son multiplos de 3.
Un numero es multiplo de 3 si la suma de sus digitos da 3, 6 o 9 y en caso tal de que la suma de un número de más de un digito se debe repetir el algoritmo hasta que de un número de un solo digito, por lo que se necesita una función que sume los digitos hasta que la suma de estos sea un número menor que 10 ya que si es un número menor que 10 obligatoriamente tendra un solo digito, despues se evalua si es 3, 6 o 9 en caso de que sea así sabremos que el número es multiplo de 3.
>
##### Ejemplo:

$$345\rightarrow 3+4+5=12\rightarrow 1+2 = 3$$

>Por ende 345 es multiplo de 3 ya que al aplicar el algoritmo mencionado el resultado final es 3, ya sabiendo esto planteamos una función que permita sumar los digitos hasta que de como resultado un número de un solo digito y despues otra función que evalue si son o no son multiplos de 3 es decir sean 3, 6 o 9.
>
```
def sumar_digitos(numero:int):
    suma = 0
    while numero > 0:
        suma += numero % 10 
        numero //= 10  
    if suma > 9:
        sumar_digitos(suma) 
    return suma
def multiplo_3(numero:int):
    suma_digitos : int = sumar_digitos(numero)
    multiplos = [3,6,9] 
    if suma_digitos in multiplos:
        return True 
    else:
        return False
```
>PDT : Hicimos un poquito de trampa ya que el codigo utiliza el operador modulo(%), pero teniendo en cuenta que solamente se utiliza para encontrar la suma de los digitos y no evaluar si un número es multiplo de 3 consideramos que es valido.

Ya teniendo las funciones necesarias para evaluar si un número es multiplo de 3, necesitaremos otra función que compare los elementos de una lista, tome los elementos que son multiplos de 3, los inserte en otra lista y como resultado retorne la lista con los multiplos de 3, por ende se recorre la lista inicial, se evalua si un elemento es multiplo de 3 utilizando las funciones ya planteadas y los elementos que cumplen se agregan a la otra lista.
>
```
def lista_multiplo_3(lista):
    multiplos_de_3 = [] 
    for elemento in lista:
        if multiplo_3(elemento): 
            multiplos_de_3.append(elemento)
    return multiplos_de_3
```
###### Código
```
# Punto 10
def sumar_digitos(numero:int):
    suma = 0
    while numero > 0:
        suma += numero % 10  # Añadir el último dígito a la suma
        numero //= 10  # Eliminar el último dígito
    if suma > 9:
        sumar_digitos(suma) # La función se repetira hasta que la suma de un solo digito
    return suma
def multiplo_3(numero:int):
    suma_digitos : int = sumar_digitos(numero)
    multiplos = [3,6,9] # Los numeros que son multiplos de 3 la suma de sus digitos dan 3, 6 o 9
    if suma_digitos in multiplos:
        return True 
    else:
        return False
def lista_multiplo_3(lista):
    multiplos_de_3 = [] # Lista donde se agregan los multiplos de 3
    for elemento in lista: # Recorre la lista
        if multiplo_3(elemento): # Evalua si los elementos de la lista cumplen la condición
            multiplos_de_3.append(elemento)
    return multiplos_de_3

if __name__ == "__main__":
    Lista1 = []
    elementos_lista1 : int = int(input("Digite cuantos elementos tendra la lista: "))
    for i in range(elementos_lista1):
        numero : int = int(input("Digite un número: "))
        Lista1.append(numero)
    Lista2 = lista_multiplo_3(Lista1)
    print(f'Da los elementos {Lista1} estos son multiplos de 3: {Lista2}')

```

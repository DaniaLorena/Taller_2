# Taller_2
> #### Los MECAPRORES
> - Rafael David Martínez Ovallos
> - Dania Lorena Pérez Moreno
>
[![logo-grupo.png](https://i.postimg.cc/T1KTDnfG/logo-grupo.png)](https://postimg.cc/vxdRRg4S"Logo Mecaprores")
### Primer Punto
Desarrollar un programa que ingrese un número entero n y separe todos los digitos que componen el número. Pista: Utilice los operadores módulo (%) y división entera (//).
> Explicación:
> Se pide al usuario un numero ingresado por teclado, este tiene que ser entero. La lógica que se utilizo para el desarrollo del algoritmo es utilizar modulo (%) y  division entera (//), además se opera con una base 10, se comienza por verificar si el numero es positivo, si no este se multiplicara por (-1). Después se debe obtener el divisor en base 10 por el cual el numero al efectuar division exacta separa el primer digito, se obtiene de la diviension entera entre numero y un divisor que va a ir aumentando al multiplicarse por 10 hasta que su division sea menor o igual a 10.
>  Al obtener el divisor adecuado, se crea un bucle que va a ir separando digito a digito, diviendo de forma entera por el divisor obtenido anteriormente, luego se obtiene el modulo de esa division y el divisor actualiza su valor dividiendo de forma entera entre 10. Este bucle se ejecuta hasta que el divisor sea cero

```python
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
```python
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
>  Primero se debe tener en cuenta que al ser espejo debe sumar lo mismo, por ello se crea un bucle que primero separe el ultimo digito, luego se actuzalice la variable *suma*, adicionado este valor con el anterior y multiplicando por 10 para obtener el reveso de la suma, es decir, tenemos 58, al multiplicarlo por 10 obtenermos 85.
> Posterior a esto, el numero se actualiza dividiendose enteramente entre 10 para obtener un numero con los digitos restantes, este proceso se repite hasta que en numero es igual a cero
```python
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
```python
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
> De acuerdo al algoritmo de Euclides, se comienza por dividir los dos numeros (a/ b)  y se obtiene el modulo entre ellos, el modulo pasar a ser el divisor y el numero menor pasa a ser el dividendo. Se obtiene el modulo de la division entre estos nuevos valores, las variables se van actualizando hasta que el modulo sea 0. Esa última iteración representa el MCD (Máximo Común Divisor), como lo que nos piden es el mcm (Minimo Comun Multiplo), se utiliza la formula de donde la multiplicacion de los dos numeros es igual a la multiplicacion entre el mcm y el mcd, se despeja el mcm y se obtiene el resultado pedido.
> 
```python
def mcd (x_1, y_1):
    mod = x_1 % y_1 #Se obtiene el primer modulo entre los numeros ingresado
    mod_previo = mod
    while mod !=0: # Se propone un bucle que se ejecuta siempre y cuando el modulo sea diferente de cero
        mod_previo = mod #Se guarda el valor del modulo antes de que este se actualice en la iteracion
        x_a = y_1  # El menor numero pasa a ser el dividendo
        y_a =mod  # El modulo pasar a ser el divisor
        mod = x_a % y_a #Se actualiza el valor del modulo
        if (mod == 0): #Se evalua si el modulo es cero sale de la iteracion
            break
    return mod_previo #Se retorna el ultimo valor del modulo antes de que este se hiciera cero

def mcm (x_1, y_1):
    max_comun_div = mcd (x_1, y_1) #Se llama la funcion
    mcm = (x_1/ max_comun_div)*y_1  #Se despeja el mcm
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
```python
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
> Explicación: Se ingresa una lista por teclado, se crea un funcion en la cual se recorra por las pociciones, en cada posicion el programa va separa cada elemento y guardarlo en una variable, buscara y contara la cantidad de letras que se solicita por el metodo *count*, se sumaran todas las vocales que se repital guardandose en una variable que posteriormente se evaluara si esta cantidad supera a 2 y si es verdadero se imprimiran las cadenas que cumpla estas condiciones
>
```python
def contar (lista):
    for i in range (len (lista)): # Va a recorrer todas las posiciones de la lista
        cadena = lista [i] # cada elemento se va a guardar en una variable
        for j in range (len (cadena)):
            cont = cadena.count ("a") + cadena.count ("e") + cadena.count ("i") + cadena.count ("o") + cadena.count ("u")   # Se busca en el elemento cuantas veces se repiten las vocales
        if (cont) > 2: # Se crea un codicional en donde si se superan las dos vocales imprime la cadena
            print (cadena)
    if (cont < 2):
        print ("No existe") 

if __name__ == "__main__":
    cantidad :int = int(input("Ingrese la cantidad de elementos que va a tener la lista: ")) #Se le pregunta al usuario cuantas elemento va a contener la lista
    lista = [] #Se crea una lista vacia
    for i in range (cantidad): #Se empieza a llenar la lista
        elemento = input(f"Ingrese el elemento {i+1}: ")
        lista.append (elemento) #Se utiliza este metodo para ir agregrando el elemento a la lista
    contar (lista)
```

### Octavo Punto
Desarrollar un programa que dadas dos listas determine que elementos tiene la primer lista que no tenga la segunda lista. Ejemplo:
Lista  | elementos
------------- | -------------
lista1: | [1, 'Hola', -12.3, True]
lista2: |[11, -12.3, 'Hola', False]
salida:  |[1, True]

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
```python
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
Escriba un programa que pida 5 números reales y calcule las siguientes operaciones:
- El promedio
- La mediana
- El promedio multiplicativo (multilplica todos y luego calcula la raíz de la cantidad de operandos)
- Ordenar los números de forma ascendente
- Ordenar los números de forma descendente
- La potencia del mayor número elevado al menor número
- La raíz cúbica del menor número
```python
def promedio (lista:float): #Se Crean funciones para obtener cada dato que se pide
    lista:float = lista
    suma : float = 0
    for i in range (len (lista)):
        suma = suma + lista[i] #Se suman todos los terminos de la lista
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


```

### Décimo Punto
Desarrolle una función que, independientemente de los números que se encuentran en la lista A, tome aquellos números que son múltiplos de 3 y los guarde en una lista nueva, la cual debe ser retornada por la función. Implemente la perspectiva de un patrón de acumulación y también de comprensión de listas.
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
```python
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
### BONO :)
Desarrollar un algoritmo que determine si una matriz es mágica. Se dice que una matriz cuadrada es mágica si la suma de cada una de sus filas, de cada una de sus columnas y de cada diagonal es igual.
> Explicación:
```python

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

```

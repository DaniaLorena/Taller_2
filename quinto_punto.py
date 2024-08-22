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

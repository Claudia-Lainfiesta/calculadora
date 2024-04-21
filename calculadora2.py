# Creadores:
# Hamlet Oswaldo Pernilla De Leon - 24007273 - BN
# María Claudia Lainfiesta Herrera - 24000149 - BN

#SUBRUTINAS DE OPERACIONES DE DOS NÚMEROS
#Subrutina --> suma de números
def operacion_suma(num1, num2):
    suma = num1 + num2
    return suma

#Subrutina --> resta de  números
def operacion_resta(num1, num2):
    resta = num1 - num2
    return resta

#Subrutina --> multiplicación de  números
def operacion_multiplicacion(num1, num2):
    multiplicacion = num1 * num2
    return multiplicacion

#Subrutina --> división de  números
def operacion_division(num1, num2):
    division = num1 // num2
    return division

#SUBRUTINAS DE OPERACIONES ESPECIALES
#Subrutina --> cociente de números
def operacion_cociente(num1, num2):
    if num2 == 0:
        error_division = "Indefinido"
        return error_division
    else:
        num_cociente = num1 // num2
        return num_cociente

#Subrutina --> residuo de números
def operacion_residuo(num1, num2):
    if num2 == 0:
        error_division = "Indefinido"
        return error_division
    else:
        num_residuo = num1 % num2
        return num_residuo

#SUBRUTINAS DE OPERACIONES DE UN NÚMERO
#Subrutina --> raíz de número
def operacion_raiz(num):
    from math import sqrt
    num_raiz = sqrt(num)
    return num_raiz

#Subrutina --> al cuadrado de número
def operacion_cuadrado(num):
    num_cuadrado = num * num
    return num_cuadrado

#Subrutina --> seno de número
def operacion_seno(num):
    from math import sin
    from math import pi
    numero1 = (num * pi)/180
    num_sen =float(sin(numero1))
    num_seno = round(num_sen, 5)
    return num_seno

#Subrutina --> coseno de número
def operacion_coseno(num):
    from math import cos
    from math import pi
    numero1 = (num * pi)/180
    num_cosen = cos(numero1)
    num_coseno = round(num_cosen, 5)
    return num_coseno

#Subrutina --> tangente de número
def operacion_tangente(num):
    from math import tan
    from math import pi
    if (operacion_coseno(num)) == 0:
        error_division = "Indefinido"
        return error_division
    else:
        num_tangente = (operacion_seno(num)) / (operacion_coseno(num))
        return num_tangente

#SUBRUTINAS DE OPERACIONES ESPECIALES
#Subrutina --> factorial de un número
def operacion_factorial(num):
    num_factorial = 1
    contador = 1
    while contador <= num:
        num_factorial = num_factorial * contador
        contador = contador + 1
    return num_factorial


#--------------------------------------------------------------------------------------------------------
def main():
    #Inicio de programa, información básica
    print("CREADORES: \n Hamlet Oswaldo Pernilla De Leon - 24007273 - BN \n María Claudia Lainfiesta Herrera - 24000149 - BN")
    print("------------------------------------------------------")
    print("¡BIENVENIDO A CODECALC! \n Ingrese su operación con la siguiente sintaxis: (operador numero1 numero2) \n Por ejemplo: (+ 1 2) ó (! 5)")
    print("--------------------------------------------------------------------------")
    #Ciclos infinitos
    while True:
        #Petición de operación a usuario guardandose en variable "operacion"
        operacion = input("calculadora>> ")
        lista = operacion.split()
        #IF para validar cuantos elementos tiene la lista y saber como proceder
        if len(lista) == 1 and operacion == "quit":
            print("Saliendo del programa...")
            print("Gracias por usar CODECALC.")
            break
        elif len(lista) == 2 and operacion != "quit":
            #Separación de las dos partes principales
            parte1 = lista[0]
            parte2 = lista[1]
            #Separación de cada uno de los caracteres
            parentesisO = parte1[0]
            signo = parte1[1:]
            num = float(parte2[:-1])
            parentesisO = parte2[-1]
            #*print(lista, parte1, parte2, parentesisO, signo, num)
            #IF para cada uno de las opciones de operaciones con un número
            if signo == "sqroot":
                #IF el número del usuario es positivo o 0 se realizara la operacion.
                if num >= 0:
                    resultado = operacion_raiz(num)
                    print("resultado>> ", resultado)
                else:
                    print("ERROR! Raiz negativa")
            elif signo == "sqr":
                resultado = operacion_cuadrado(num)
                print("resultado>> ", resultado)
            elif signo == "sin":
                resultado = operacion_seno(num)
                print("resultado>> ", resultado)
            elif signo == "cos":
                resultado = operacion_coseno(num)
                print("resultado>> ", resultado)
            elif signo == "tan":
                resultado = operacion_tangente(num)
                print("resultado>> ", resultado)
            elif signo == "!":
                resultado = operacion_factorial(num)
                print("resultado>> ", resultado)
            else:
                print("Operación no válida.")
        elif len(lista) == 3 and operacion != "quit":
            #Separación de las tres partes principales
            parte1 = lista[0]
            parte2 = lista[1]
            parte3 = lista[2]
            #Separación de cada uno de los caracteres
            parentesisO = parte1[0]
            signo = parte1[1:]
            num1 = float(parte2[0:])
            num2 = float(parte3[:-1])
            parentesisF = parte3[-1]
            print(parentesisO,signo,num1,num2,parentesisF)
            if signo == "+":
                resultado = operacion_suma(num1, num2)
                print("resultado>> ", resultado)
            elif signo == "-":
                resultado = operacion_resta(num1, num2)
                print("resultado>> ", resultado)
            elif signo == "*":
                resultado = operacion_multiplicacion(num1, num2)
                print("resultado>> ", resultado)
            elif signo == "/":
                if num2 != 0:
                    resultado = operacion_division(num1, num2)
                    print("resultado>> ", resultado)
                else:
                    print("ERROR! Divisón entre 0")
            elif signo == "div":
                resultado = operacion_cociente(num1, num2)
                print("resultado>> ", resultado)
            elif signo == "%":
                resultado = operacion_residuo(num1, num2)
                print("resultado>> ", resultado)
            else:
                print("ERROR! Operación no valida")
        else:
            print("ERROR!")


main()
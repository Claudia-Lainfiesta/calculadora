# Creadores:
# Hamlet Penilla
# María Claudia Lainfiesta Herrera

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

#Subrutina --> factorial de un número
def operacion_factorial(num):
    num_factorial = 1
    contador = 1
    while contador <= num:
        num_factorial = num_factorial * contador
        contador = contador + 1
    return num_factorial

def main():
    #Inicio de programa, información básica
    print("CREADORES: ")
    print("Hamlet Oswaldo Pernilla De Leon - 24007273 - BN")
    print("María Claudia Lainfiesta Herrera - 24000149 - BN")
    print("-------------------------------------------")
    print("¡BIENVENIDO A CODECALC!")
    print("Ingrese su operación con la siguiente sintaxis: (operador numero1 numero2)")
    print("Por ejemplo: (+ 1 2)")
    print("--------------------------------------------------------------------------")

    while True:
        #Ingreso de operación desde el usuario
        operacion = input("calculadora>> ")
        #Separación en lista de la operación
        listanum = operacion.split()
        #Despliega la lista separada
        print("Lista split", listanum)
        #If que verifica si el usuario desea salir del programa
        if operacion == "quit":
            print("Saliendo del programa, hasta luego...")
            break
        #If que valida si el usuario ingreso una operación o solamente un número
        elif len(listanum) == 3:
            #División de lista
            parte1 = listanum[0] #(operador
            parte2 = listanum[1] #num1
            parte3 = listanum[2] #num2)
            #División de cada string
            parentesisO = parte1[0]
            operador = parte1[1]
            num1 = float(parte2[0])
            num2 = float(parte3[0])
            parentesisF = parte3[1]
            #If para valida primero si tiene paréntesis al inicio y final, y luego verificar todas las operacion con dos números en su sintaxis
            if parentesisO == "(" and parentesisF == ")":
                #If para validar cada uno de los signo y realizar la operación correspondiente
                if operador == "+":
                    resultado = operacion_suma(num1, num2)
                    print("resultado>> ", resultado)
                elif operador == "-":
                    resultado = operacion_resta(num1, num2)
                    print("resultado>> ", resultado)
                elif operador == "*":
                    resultado = operacion_multiplicacion(num1, num2)
                    print("resultado>> ", resultado)
                elif operador == "/":
                    if num2 > 0:
                        resultado = operacion_division(num1, num2)
                        print("resultado>> ", resultado)
                    else:
                        print("ERROR! División entre cero.")
            else:
                print("¡ERROR! Expresión no válida.")
        elif len(listanum) == 2:
            #División de lista
            parte1 = listanum[0] #(operador
            parte2 = listanum[1] #num1)
            #División de cada string
            parentesisO = parte1[0]
            operador = parte1[1]
            num1 = float(parte2[0])
            parentesisF = parte2[1]
            #If para valida primero si tiene paréntesis al inicio y final, y luego verificar todas las operacion con dos números en su sintaxis
            if parentesisO == "(" and parentesisF == ")":
                #If para validar cada uno de los signo y realizar la operación correspondiente
                if operador == "sqroot":
                    if num1 >= 0:
                        resultado = operacion_raiz(num1)
                        print("resultado>> ", resultado)
                    else:
                        print("ERROR! Raiz cuadrada negativa")
                elif operador == "sqr":
                    resultado = operacion_cuadrado(num1)
                    print("resultado>> ", resultado)
                elif operador == "sin":
                    resultado = operacion_seno(num1)
                    print("resultado>> ", resultado)
                elif operador == "cos":
                    resultado = operacion_coseno(num1)
                    print("resultado>> ", resultado)
                elif operador == "tan":
                    resultado = operacion_tangente(num1)
                    print("resultado>> ", resultado)
            else:
                print("¡ERROR! Expresión no válida.")
        elif len(listanum) == 1:
            print("resultado>> ", operacion)
        else:
            print("¡ERROR! Expresión no válida.")
main()
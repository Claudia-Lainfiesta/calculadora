# Creadores:
# Hamlet Oswaldo Pernilla De Leon - 24007273 - BN
# María Claudia Lainfiesta Herrera - 24000149 - BN
#--------------------------------------------------------------------------------------
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
    #If que valida que el segundo numero 0 o no.
    if num2 == 0:
        error_division = "ERROR! "+ str(num1) + " dividido " + str(num2) + " es indefinido."
        return error_division
    else:
        division = num1 / num2
        return division
#SUBRUTINAS DE OPERACIONES DE UN NÚMERO
#Subrutina --> raíz de número
def operacion_raiz(num):
    from math import sqrt
    #If que valida que el numero no sea negativo
    if num >= 0:
        num_raiz = sqrt(num)
        return num_raiz
    else:
        error_raiz = "ERROR! el número " + str(num) + " es indefinido por ser negativo."
        return error_raiz
#Subrutina --> al cuadrado de número
def operacion_cuadrado(num):
    num_cuadrado = num * num
    return num_cuadrado
#Subrutina --> seno de número
def operacion_seno(num):
    from math import sin
    from math import pi
    #Conversión del numero de radianes a grados
    numero1 = (num * pi)/180
    num_sen =float(sin(numero1))
    num_seno = round(num_sen, 5)
    return num_seno
#Subrutina --> coseno de número
def operacion_coseno(num):
    from math import cos
    from math import pi
    #Conversión del numero de radianes a grados
    numero1 = (num * pi)/180
    num_cosen = cos(numero1)
    num_coseno = round(num_cosen, 5)
    return num_coseno
#Subrutina --> tangente de número
def operacion_tangente(num):
    from math import tan
    from math import pi
    #If que valida que la respuesta sea indefinida o no
    if (operacion_coseno(num)) == 0:
        error_division = "ERROR! la tangente de " + str(num) + " es indefinido."
        return error_division
    else:
        num_tangente = (operacion_seno(num)) / (operacion_coseno(num))
        return num_tangente
#SUBRUTINAS DE OPERACIONES ESPECIALES
#Subrutina --> cociente de números
def operacion_cociente(num1, num2):
    #If que valida que el segundo numero sea 0 no
    if num2 == 0:
        error_division = "ERROR! el cociente de "+ str(num1) + " entre " + str(num2) + " es indefinido."
        return error_division
    else:
        num_cociente = num1 // num2
        return num_cociente
#Subrutina --> residuo de números
def operacion_residuo(num1, num2):
    #If que valida que el segundo numero sea 0 no
    if num2 == 0:
        error_division = "ERROR! el residuo de "+ str(num1) + " entre " + str(num2) + " es indefinido."
        return error_division
    else:
        num_residuo = num1 % num2
        return num_residuo
#Subrutina --> factorial de un número
def operacion_factorial(num):
    if num - int(num) == 0:
        if num == 0:
            cero_f = 1
            return cero_f
        elif num < 0:
            fact_negativo = "ERROR! " + str(num) + " no es un entero positivo."
            return fact_negativo
        else:
            num_factorial = 1
            contador = 1
            while contador <= num:
                num_factorial = num_factorial * contador
                contador = contador + 1
            return num_factorial
    else:
        a = "ERROR! " + str(num) + " no es un entero entero."
        return a
#-----------------------------------------------------------------------------
#SUBRUTINA DE VALIDACIÓN DE PARENTESIS
def verificar_parentesis(lista):
    #Lista llamada pila
    pila = []
    #For que barre toda la lista y verifica que los parentesis sean correctos
    for caracter in lista:
        if caracter == '(':
            pila.append(caracter)
        elif caracter == ')':
            if not pila:
                return False  # Hay un ')' sin un '(' correspondiente
            pila.pop()  # Remover '(' de la pila

    return len(pila) == 0  # La pila debe estar vacía para que los paréntesis estén balanceados
#SUBRUTINA DE VALIDACIÓN DE OPERADORES
def evaluacion(operacion):
    lista = operacion.split()
    #Almacenar en una variable el resultado de la subrutina de validación de cantidades de paréntesis
    validacionparentesis = verificar_parentesis(lista)
    print(lista)
    #Si el usuario ingresa algo que no sea un numero no realizara la operación
    try:
        if validacionparentesis == True:
            #IF para validar cuantos elementos tiene la lista y saber como proceder
            if len(lista) == 1 and operacion != "quit":
                try:
                    operacion = float(operacion)
                    return operacion
                except ValueError:
                    return "ERROR! Ingreso letras, solo se aceptan números"
            elif len(lista) == 2 and operacion != "quit":
                #Separación de las dos partes principales
                parte1 = lista[0]
                parte2 = lista[1]
                #Separación de cada uno de los caracteres
                parentesisO = parte1[0]
                signo = parte1[1:]
                num = float(parte2[:-1])
                parentesisF = parte2[-1]
                if parentesisO == "(" and parentesisF == ")":
                    #IF para cada uno de las opciones de operaciones con un número
                    if signo == "sqroot":
                        return operacion_raiz(num)
                    elif signo == "sqr":
                        return operacion_cuadrado(num)
                    elif signo == "sin":
                        return operacion_seno(num)
                    elif signo == "cos":
                        return operacion_coseno(num)
                    elif signo == "tan":
                        return operacion_tangente(num)
                    elif signo == "!":
                        return operacion_factorial(num)
                    else:
                        return "Operación no válida."
                else:
                    return "Operación no válida por parentesis"
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
                #print(parentesisO,signo,num1,num2,parentesisF)
                if parentesisO == "(" and parentesisF == ")":
                    if signo == "+":
                        return operacion_suma(num1, num2)
                    elif signo == "-":
                        return operacion_resta(num1, num2)
                    elif signo == "*":
                        return operacion_multiplicacion(num1, num2)
                    elif signo == "/":
                        return operacion_division(num1, num2)
                    elif signo == "div":
                        return operacion_cociente(num1, num2)
                    elif signo == "%":
                        return operacion_residuo(num1, num2)
                    else:
                        return "ERROR! Operación no valida"
                else:
                    return "ERROR! Operación no válida por parentesis"
            else:
                return "ERROR! Operación no válida"
        elif validacionparentesis == False:
            return "ERROR! Los parentesis no son válidos"
    except ValueError:
        return "ERROR! Operación no válida."
#-------------------------------------------------------------------------------------------
#SUBRUTINA PRINCIPAL
def main():
    #Inicio de programa, información básica
    print("CREADORES: ")
    print("Hamlet Oswaldo Pernilla De Leon - 24007273 - BN")
    print("María Claudia Lainfiesta Herrera - 24000149 - BN")
    print("----------------------------------------------------")
    print("¡BIENVENIDO A CODECALC!")
    print("Ingrese su operación con la siguiente sintaxis: (operador numero1 numero2)")
    print("Por ejemplo: (+ 1 2)")
    print("Para salir del programa ingrese la palabra 'quit'")
    print("--------------------------------------------------------------------------")
    #Ciclo infinito para que trabaje infinitamente
    while True:
        #Petición de operación a usuario guardándose en variable "operacion"
        operacion = input("calculadora>> ")
        #If que si el usuario ingresa la palabra "quit" se acabara el programa
        if operacion == "quit":
            print("Saliendo del programa...")
            print("Gracias por usar CODECALC.")
            break
        else:
            resultado = evaluacion(operacion)
            print("resultado>>", resultado)

main()
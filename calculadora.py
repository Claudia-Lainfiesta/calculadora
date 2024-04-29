# Creadores:
# Hamlet Oswaldo Pernilla De Leon - 24007273 - BN.
# María Claudia Lainfiesta Herrera - 24000149 - BN.
#---------------------------------------------------------------------------------------------
#SUBRUTINAS DE OPERACIONES DE DOS NÚMEROS.
#Subrutina --> suma de números.
def operacion_suma(num1, num2):
    suma = num1 + num2
    return suma
#Subrutina --> resta de  números.
def operacion_resta(num1, num2):
    resta = num1 - num2
    return resta
#Subrutina --> multiplicación de  números.
def operacion_multiplicacion(num1, num2):
    multiplicacion = num1 * num2
    return multiplicacion
#Subrutina --> división de  números.
def operacion_division(num1, num2):
    #If que valida que el segundo numero 0 o no.
    if num2 == 0:
        error_division = "ERROR! "+ str(num1) + " dividido " + str(num2) + " es indefinido."
        return error_division
    else:
        division = num1 / num2
        return division
#SUBRUTINAS DE OPERACIONES DE UN NÚMERO.
#Subrutina --> raíz de número.
def operacion_raiz(num):
    from math import sqrt
    #If que valida que el numero no sea negativo.
    if num >= 0:
        num_raiz = sqrt(num)
        return num_raiz
    else:
        error_raiz = "ERROR! el número " + str(num) + " es indefinido por ser negativo."
        return error_raiz
#Subrutina --> al cuadrado de número.
def operacion_cuadrado(num):
    num_cuadrado = num * num
    return num_cuadrado
#Subrutina --> seno de número.
def operacion_seno(num):
    from math import sin
    from math import pi
    #Conversión del numero a grados.
    numero1 = (num * pi)/180
    num_sen =float(sin(numero1))
    num_seno = round(num_sen, 5)
    return num_seno
#Subrutina --> coseno de número.
def operacion_coseno(num):
    from math import cos
    from math import pi
    #Conversión del numero a grados.
    numero1 = (num * pi)/180
    num_cosen = cos(numero1)
    num_coseno = round(num_cosen, 5)
    return num_coseno
#Subrutina --> tangente de número.
def operacion_tangente(num):
    from math import tan
    from math import pi
    #If que valida que la respuesta sea indefinida o no.
    if (operacion_coseno(num)) == 0:
        error_division = "ERROR! la tangente de " + str(num) + " es indefinido."
        return error_division
    else:
        num_tangente = (operacion_seno(num)) / (operacion_coseno(num))
        return num_tangente
#SUBRUTINAS DE OPERACIONES ESPECIALES.
#Subrutina --> cociente de números.
def operacion_cociente(num1, num2):
    #If que valida que el segundo numero sea 0 no.
    if num2 == 0:
        error_division = "ERROR! el cociente de "+ str(num1) + " entre " + str(num2) + " es indefinido."
        return error_division
    else:
        num_cociente = num1 // num2
        return num_cociente
#Subrutina --> residuo de números.
def operacion_residuo(num1, num2):
    #If que valida que el segundo numero sea 0 no.
    if num2 == 0:
        error_division = "ERROR! el residuo de "+ str(num1) + " entre " + str(num2) + " es indefinido."
        return error_division
    else:
        num_residuo = num1 % num2
        return num_residuo
#Subrutina --> factorial de un número.
def operacion_factorial(num):
    if num - int(num) == 0:
        if num == 0:
            cero_f = 1
            return cero_f
        elif num < 0:
            fact_negativo = "ERROR! " + str(num) + " no es un número positivo."
            return fact_negativo
        else:
            num_factorial = 1
            contador = 1
            while contador <= num:
                num_factorial = num_factorial * contador
                contador = contador + 1
            return num_factorial
    else:
        a = "ERROR! " + str(num) + " no es un número entero."
        return a
#SUBRUTINA DE EVALUCION DE OPERACIÓN.
def evaluacion(operacion):
    #Contadores en 0 para el for.
    cont1 = 0
    cont2 = 0
    #For que cuenta la cantidad de de parentesis abiertos y cerrados.
    for letra in operacion:
        if letra == '(':
            cont1 += 1
        elif letra == ')':
            cont2 += 1
    #If son iguales proceder a operar.
    if (cont1 == cont2):
        tokens = operacion.replace('(', ' ( ').replace(')', ' ) ').split()
    else:
        return "ERROR! '" + str(operacion) + "' expresion no valida por paréntesis."
    #Subrutina recursiva para operar operaciones combinadas.
    def evaluar(tokens):
        #If si no manda el usuario regresa error.
        if len(tokens) == 0:
            return None
        token = tokens.pop(0)
        #If valida los parentesis, luego su signo y sus operadores para saber como proceder.
        if token == '(':
            resultado = evaluar(tokens)
            tokens.pop(0)
            return resultado
        elif token in {'+', '-', '*', '/', 'div', '%'}:
            operador = token
            operando1 = evaluar(tokens)
            operando2 = evaluar(tokens)
            #If que si el usuario no manda ningun numero devuelva error.
            if operando1 is None or operando2 is None:
                return "ERROR! '" + str(operacion) + "' expresion no valida, no se  ingresaron valores para operar."
            #If que dependiendo su signo realice la operación.
            if operador == '+':
                operadosuma = operacion_suma(operando1, operando2)
                return operadosuma
            elif operador == '-':
                operadoresta = operacion_resta(operando1, operando2)
                return operadoresta
            elif operador == '*':
                operadomultiplicacion = operacion_multiplicacion(operando1, operando2)
                return operadomultiplicacion
            elif operador == '/':
                operadodivision = operacion_division(operando1, operando2)
                return operadodivision
            elif operador == 'div':
                operadocociente = operacion_cociente(operando1, operando2)
                return operadocociente
            elif operador == '%':
                operadoresiduo = operacion_residuo(operando1, operando2)
                return operadoresiduo
        #IF para cada uno de las opciones de operaciones con un número.
        elif token == 'sqroot':
            operando = evaluar(tokens)
            if operando is None:
                return "ERROR! " + str(operacion) + " expresion no valida, operando faltante."
            else:
                operadoraiz = operacion_raiz(operando)
                return operadoraiz
        elif token == 'sqr':
            operando = evaluar(tokens)
            if operando is None:
                return "ERROR! " + str(operacion) + " expresion no valida, operando faltante."
            operadocuadrado = operacion_cuadrado(operando)
            return operadocuadrado
        elif token == 'sin':
            operando = evaluar(tokens)
            if operando is None:
                return "ERROR! " + str(operacion) + " expresion no valida, operando faltante."
            operadoseno = operacion_seno(operando)
            return operadoseno
        elif token == 'cos':
            operando = evaluar(tokens)
            if operando is None:
                return "ERROR! " + str(operacion) + " expresion no valida, operando faltante."
            operadocoseno = operacion_coseno(operando)
            return operadocoseno
        elif token == 'tan':
            operando = evaluar(tokens)
            if operando is None:
                return "ERROR! " + str(operacion) + " expresion no valida, operando faltante."
            operadotangente = operacion_tangente(operando)
            return operadotangente
        elif token == "!":
            operando = evaluar(tokens)
            if operando is None:
                return "ERROR! " + str(operacion) + " expresion no valida, operando faltante."
            operadofactorial = operacion_factorial(operando)
            return operadofactorial
        else:
            #Try que maneja el error si el usuario no coloca la operacion correctamente.
            try:
                return float(token)
            except ValueError:
                return None
    resultado = evaluar(tokens)
    #If que verifica si existe algun error con el input del usuario.
    if resultado is None:
        return "ERROR! '" + str(operacion) + "' expresion no valida, se ingresaron letras, operaciones incorrectas o parentesis mal colocados."
    else:
        return resultado
def main():
    #Inicio de programa, información básica.
    print("CREADORES: ")
    print("Hamlet Oswaldo Pernilla De Leon - 24007273 - BN.")
    print("María Claudia Lainfiesta Herrera - 24000149 - BN.")
    print("--------------------------------------------------------------------------")
    print("¡BIENVENIDO A CODECALC!")
    print("Ingrese su operación con la siguiente sintaxis: (operador numero1 numero2).")
    print("Por ejemplo: (+ 1 2)")
    print("Para salir del programa ingrese la palabra 'quit'.")
    print("--------------------------------------------------------------------------")
    #Ciclo infinito para que trabaje infinitamente.
    while True:
        #Petición de operación a usuario guardándose en variable "operacion".
        operacion = input("calculadora>> ")
        #If que si el usuario ingresa la palabra "quit" se acabara el programa.
        if operacion == "quit":
            print("Saliendo del programa...")
            print("Gracias por usar CODECALC.")
            break
        else:
            resultado = evaluacion(operacion)
            print("resultado>>", resultado)
main()
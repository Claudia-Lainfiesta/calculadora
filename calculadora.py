# Creadores:
# Hamlet Penilla
# María Claudia Lainfiesta Herrera

#SUBRUTINAS DE OPERACIONES
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
def operacion_raiz(num1):
    suma = num1
    return suma

def operacion_cuadrado(num1):
    suma = num1
    return suma

def operacion_seno(num1):
    suma = num1
    return suma

def operacion_coseno(num1):
    suma = num1
    return suma

def operacion_tangente(num1):
    suma = num1
    return suma

#SUBRUTINAS Claudia
def recursividad1(parentesisO, paretesisF, num1):
    for i in parentesisO:
        if parentesisO == "(" and paretesisF == ")" and num1 
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

    #Ingreso de operación desde el usuario
    operacion = input("calculadora>> ")

    #Separación en lista de la operación
    listanum = operacion.split()
    while operacion == "quit":
        print("Saliendo...")
        break
    else:
        #Despliega la lista separada
        print("Lista split", listanum)


        #If que valida si el usuario ingreso una operación o solamente un número
        if len(listanum) == 3:
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
                    resultado = operacion_division(num1, num2)
                    print("resultado>> ", resultado)
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
                    resultado = operacion_raiz(num1)
                    print("resultado>> ", resultado)
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
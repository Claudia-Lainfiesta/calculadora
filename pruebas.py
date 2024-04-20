importe math
def validar_operacion(operacion):
    # Eliminar espacios en blanco y dividir la operación en una lista de caracteres
    operacion = operacion.replace(" ", "")
    caracteres = list(operacion)
    
    # Función recursiva para validar la estructura de los paréntesis
    def validar_parentesis(caracteres, indice, contador):
        # Caso base: si hemos recorrido todos los caracteres
        if indice == len(caracteres):
            return contador == 0
        
        # Si encontramos un paréntesis abierto, incrementamos el contador
        if caracteres[indice] == "(":
            return validar_parentesis(caracteres, indice + 1, contador + 1)
        # Si encontramos un paréntesis cerrado, decrementamos el contador
        elif caracteres[indice] == ")":
            return validar_parentesis(caracteres, indice + 1, contador - 1)
        # Si encontramos cualquier otro carácter, continuamos sin modificar el contador
        else:
            return validar_parentesis(caracteres, indice + 1, contador)
    
    # Verificar que los paréntesis iniciales y finales sean correctos
    if caracteres[0] == "(" and caracteres[-1] == ")" and caracteres.count("(") == caracteres.count(")"):
        return validar_parentesis(caracteres, 0, 0)
    else:
        return False

# Ejemplo de uso
operacion = "()(+ num1 num2)))"
if validar_operacion(operacion):
    print("La operación es válida.")
else:
    print("La operación no es válida.")

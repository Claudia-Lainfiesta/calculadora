elif (len(lista)-1) % 2 == 0 and operacion != "quit":
                    mitad = len(lista) // 2
                    for i in range(1, mitad + 1):
                        parte1 = lista[(i)*-1]
                        parte2 = lista[(i * 2)*-2]
                        parte1 = parte1[:((mitad)*-1)]
                        num1 = float(parte2)
                        num2 = float(parte1)
                        signo = lista[((i * 2)*-1) - 1][1:]  # Eliminar el primer carácter, que es '('
                        

                        if signo == "+":
                            resultado = operacion_suma(num1, num2)
                        elif signo == "-":
                            resultado = operacion_resta(num1, num2)
                        elif signo == "*":
                            resultado = operacion_multiplicacion(num1, num2)
                        elif signo == "/":
                            resultado = operacion_division(num1, num2)
                        elif signo == "div":
                            resultado = operacion_cociente(num1, num2)
                        elif signo == "%":
                            resultado = operacion_residuo(num1, num2)
                        else:
                            return "ERROR! Operación no valida"
                        lista = lista[:(mitad*-1)]  # Eliminar el último elemento de la lista
                        lista[-1] = str(float(resultado)) + ")"  # Reemplazar el último elemento con el resultado 
                        return  evaluacion(' '.join(lista)) # Devolver el resultado final como un número float
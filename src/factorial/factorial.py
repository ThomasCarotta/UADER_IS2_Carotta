#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

# Función para calcular el factorial de un número
def factorial(num): 
    if num < 0: 
        print("Factorial de un número negativo no existe")
    elif num == 0: 
        return 1
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

# Verifica si se proporcionan suficientes argumentos en la línea de comandos
if len(sys.argv) < 2:
    print("Debe ingresar dos números en el formato 'desde-hasta'.")
    sys.exit(1)

# Obtiene los números de inicio y fin del rango desde la línea de comandos
numeros = sys.argv[1].split('-')
desde = int(numeros[0])
hasta = int(numeros[1])

# Verifica si el límite inferior está dentro del rango permitido
if desde < 1:
    print("El límite inferior debe ser mayor o igual a 1.")
    sys.exit()

# Verifica si el límite superior está dentro del rango permitido
elif hasta > 60:
    print("El límite superior no puede ser mayor que 60.")
    sys.exit()

# Verifica si el límite inferior es mayor que el límite superior
elif desde > hasta:
    print("El límite inferior no puede ser mayor que el límite superior.")
    sys.exit()

# Verifica si el rango especificado es válido
if desde >= hasta:
    print("El primer número debe ser menor que el segundo número en el rango.")
    sys.exit(1)

# Calcula y muestra los factoriales para cada número en el rango especificado
for num in range(desde, hasta + 1):
    print("Factorial de", num, "! es", factorial(num))

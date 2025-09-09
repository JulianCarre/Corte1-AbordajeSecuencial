# Este ejercicio vale una décima del 1 corte

import math

while True:
    numero = input("Introduce un número (o escribe 'salir' para terminar): ")
    if numero.lower() == 'salir':
        print("Programa terminado.")
        break
    try:
        numero = int(numero)
        # Verificación primo
        if numero > 1:  
            es_primo = True
            for i in range(2, int(math.sqrt(numero)) + 1):
                if numero % i == 0:
                    es_primo = False
                    break
            if es_primo:
                print(f" {numero} es PRIMO")
            else:
                print(f" {numero} NO es primo")
        else:
              if numero == 1:
                 print(f" {numero} es PRIMO")
    except ValueError:
        print(" Por favor, ingresa un número válido.")

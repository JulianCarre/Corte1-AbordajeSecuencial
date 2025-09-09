# Este ejercicio vale una decima del 1 corte 
while True:
    numero = input("Introduce un número (o escribe 'salir' para terminar): ")
    if numero.lower() == 'salir':
        print("Programa terminado.")
        break
    try:
        numero = int(numero)
        if numero % 2 == 0:
            print(f"  {numero} es par")
        else:
            print(f"  {numero} es impar")
    except ValueError:
        print("Por favor, ingresa un número válido.")

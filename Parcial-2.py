print("*****************************") 
print("Bienvenido a nuestro programa")
print("*****************************")

while True:
    try:
        n = int(input("\nIngrese un numero positivo: "))
        if n <= 0:
            print("\nDebe ingresar un número que sea mayor a cero")
            continue
        break
    except ValueError:
        print("\nEl dato no es valido, debe ingresar un valor tipo entero mayor a cero")

if n > 0:
    suma = 0

for i in range(1, n + 1):
    suma += 1 / i

print('La suma de la serie es: ', suma)

print('Fin del programa')
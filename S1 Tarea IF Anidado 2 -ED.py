#Leer tres números enteros diferentes entre sí y determinar el número
#mayor de los tres.
print("---Calcular numero mayor---")
n1=int(input("Ingrese numero 1: "))
n2=int(input("Ingrese numero 2: "))
n3=int(input("Ingrese numero 3: "))
if n1 > n2 and n1 > n3:
    mayor= n1
else:
    if n2 > n3:
        mayor = n2
    else:
        mayor = n3
print("Numero mayor", mayor)
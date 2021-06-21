#Determinar si un número entero proporcionado por el usuario
#es primo. Un número primo es un entero que no tiene más divisores
# que él mismo y la unidad.
num=int(input("Ingrese un numero entero: "))
primo=True
divisor=2
while divisor < num and primo==True:
    res = num % divisor
    if res == 0:
        primo= False
    divisor=divisor+1
if primo == True:
    print("Numero {} es primo".format(num))
else:
    print("Numero {} no es primo".format(num))
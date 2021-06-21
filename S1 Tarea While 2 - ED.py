#Diseñe un código para calcular la suma y producto de N números enteros,
#utilizando un bucle controlado por el usuario.
resp=input("Desea ingresar? (S/N) ").lower()
num=int(input("Ingrese un numero: "))
suma=0
prod=1
while resp == "s":
    suma = suma + num
    prod = prod * num
    print(suma, prod)
    resp=input("Desea continuar? (S/N) ").lower()
print("Total de la suma es: ", suma)
print("Total del producto es: ", prod)
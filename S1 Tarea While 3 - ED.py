#Diseñe un código para calcular la suma y producto de
#N números enteros, utilizando un bucle controlado por centinela.
num=int(input("Ingrese un numero: "))
resp=input("Ingrese una letra: ").lower()
suma=0
prod=1
while resp != "a":
    suma = suma + num
    prod = prod * num
    print(suma, prod)
    resp=input("Ingrese una letra ").lower()
print("Total de la suma es: ", suma)
print("Total del producto es: ", prod)
#Aplicar las fases  para  la resolución de un problema
# para leer un vector de 20 números enteros y a continuación
# escribir en un vector A todos los números negativos y en un
# vector B todos los positivos o iguales a cero. Imprimir dichos
# vectores.
listaB=[]
listaA=[]
listanumeros=[]
n=5
for x in range(n):
    numero=int(input("Ingrese numero: "))
    listanumeros.append(int(numero))
for i in listanumeros:
    if i > 0:
        listaB.append(i)
    else:
        listaA.append(i)
print(listaA)
print(listaB)
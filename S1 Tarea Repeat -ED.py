#Aplicar los pasos de la metodología para la solución
# de un problema para leer un número entero N y calcular el
# resultado de la siguiente serie:
# 1 – 1/2+ 1/3 – 1/4 +.... +/- 1/N
serie=0
I = 1
N=int(input("Ingrese un numero: "))
band=True
while I<N:
    if band == True:
        serie=serie+(1/I)
        band==False
    else:
        serie=serie-(1/I)
        band==True
    I=I+1

print(serie)
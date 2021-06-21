#Calcular el factorial de N números enteros leídos de
# teclado. El problema consistirá en realizar una estructura
# de N iteraciones aplicando el factorial de un número
#n=input("Ingrese n: ")
n=10
num=0
i=0
fact=1
for i in range(n):
    num=num+1
    print("num",num)
    for j in range(num):
        fact=num*num
        print("fact",fact)


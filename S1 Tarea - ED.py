#Encontrar la superficie de un circulo para un radio cualquiera
print("---Calcular superficie de un circulo---")
PI=3.1416
R=float(input("Ingrese Radio: "))
S= (PI*R)**2
print("Superficie", S)

#En una tienda se ofrece un descuento del 15% sobre el total de la compra
# y un cliente desea saber cuánto deberá pagar finalmente por su compra.
print("---Calcular Descuento---")
TC=float(input("Ingrese total compra: "))
D=TC*0.15
CP=TC-D
print("Descuento: ", CP)

#Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas.
# El vendedor desea saber cuánto dinero obtendrá por concepto de comisiones por
# las tres ventas que realiza en el mes y el total que recibirá en el mes tomando
# en cuenta su sueldo base y sus comisiones.
print("---Calcular pago mas comision---")
SB=float(input("Ingrese sueldo base: "))
V1=float(input("Ingrese primera venta: "))
V2=float(input("Ingrese segunda venta: "))
V3=float(input("Ingrese tercera venta: "))
TV=V1+V2+V3
C=TV*0.1
TR=SB+C
print("Total al mes: ", TR)


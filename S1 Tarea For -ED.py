#Calcular la suma de los cuadrados de los primeros 100 enteros y escribir el resultado.
print("---Calcular la suma de los cuadrados de los primeros 100 enteros---")
suma=0
for i in range(100):
    suma = suma + i*i
print("Total: ",suma)

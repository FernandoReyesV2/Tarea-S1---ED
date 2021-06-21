#Construir un algoritmo tal, que dado como dato la calificación de un alumno en un
# examen, escriba si está aprobado.
print("---Presentar si un estudiante aprueba---")
Cal=float(input("Ingrese Calificacion: "))
if Cal >= 7:
    print("Aprobado")

#Dado como dato la calificación de un alumno en un examen, escriba “aprobado”
# si su calificación es mayor o igual que 7 y “Reprobado” en caso contrario.
print("---Presentar si un estudiante aprueba o no---")
Cal2=float(input("Ingrese Calificacion: "))
if Cal2 >= 7:
    print("Aprobado")
else:
    print("Reprobado")

#Dado el sueldo de un empleado, encontrar el nuevo sueldo si obtiene un aumento
# del 10% si su sueldo es inferior a $600, en caso contrario no tendrá aumento.
print("---Calcular aumento de sueldo---")
Sueldo=float(input("Ingrese Sueldo: "))
if Sueldo<600:
    ns=Sueldo+Sueldo*0.1
else:
    ns=Sueldo
print("Nuevo Sueldo", ns)


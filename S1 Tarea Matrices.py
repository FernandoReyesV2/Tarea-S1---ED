#Se tiene información sobre las calificaciones de 6 exámenes de un grupo de 30 alumnos.
class prueba:
    def promedio_calificaion(self):
        i,j=1,1
        numeroexamenes= 6
        numerosalumnos = 2
        #numerosalumnos= int(input("Escriba el numero de alumnos: "))
        sum =0
        mayor = 1
        for i in range(numerosalumnos):
            i = i + 1
            for j in range(numeroexamenes):
                j=j+1
                cal=int(input("Escriba la calificacion del alumno {} en el examen {} ".format(i,j)))
                sum = sum + cal
                if cal > mayor:
                    mayor=cal
                    examen = j
                    alumno = i
                if j > 5:
                    print("-----------------")
        for j in range(numerosalumnos):
            for i in range(numeroexamenes):
                prom = sum / (numeroexamenes*2)
        print("Promedio Examen: ", prom)


        for j in range(numeroexamenes):
            for i in range(numerosalumnos):
                prom = sum / (numerosalumnos)
        print("Promedio del Alumno: ", prom)

        print("El examen {} del alumno {} obtuvo el mayor promedio {}".format(examen,alumno,mayor))
proof = prueba()
proof.promedio_calificaion()
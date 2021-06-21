#Determinar la cantidad de dinero que recibirá un trabajador por concepto de las
#horas extras trabajadas en una empresa, sabiendo que cuando las horas de trabajo
#exceden de 40, el resto  se consideran horas extras y que éstas se pagan al doble
#de una hora normal cuando no exceden de 8;  si las horas extras exceden de 8 se
#pagan las primeras 8 al  doble de lo que se paga por una hora normal y el resto
# al triple.
print("---Calcular pago por horas extra---")
horastrabajadas=int(input("Ingrese horas trabajadas: "))
pagoporhora=int(input("Ingrese pago por horas: "))
if horastrabajadas > 40:
    horasextra = horastrabajadas - 40
    if horasextra > 8:
        horasextratrabajadas = horasextra * 8
        pagohoraextra=pagoporhora*2*8+pagoporhora*3*horasextratrabajadas
    else:
        pagohoraextra=pagoporhora*2*horasextra
    total= pagoporhora*40+ pagohoraextra
else:
    total=pagoporhora*horastrabajadas
print("Total: ",total)
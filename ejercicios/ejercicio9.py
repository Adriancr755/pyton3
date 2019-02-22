print ("bienvenido al programa: ".center (50, "-"))
print ("la Hora extra son de 10 Quetzales")
print ("la hora de trabajo son de 20 Quetzales")
hora = 0
Horas_extra = 0
SUELDO_HORAS_EXTRA = 10
HORAS_DE_TRABAJO = 20
pago = 0
total = 0 
hora = int(input("ingrese las horas de trabajo: "))
Horas_extra = int(input("ingrese sus horas extra"))
pago = pago + int(hora * HORAS_DE_TRABAJO)
total = total + int(Horas_extra * SUELDO_HORAS_EXTRA)
print ("sus horas de trabajo son de: ",pago)
print ("su sueldo de horas extra es de: ",total)






##realizar el promedio de Nnotas utilizando el for

print("bienvenido al programa".center(50, "-"))

n = 0
suma = 0
print ("ingrese las notas que quiera pulse 1 para detener: ")

cantidad = int(input("ingrese la cantidad de notas: "))
for i in range (cantidad):
    n = int(input("ingrese notas: "))
    suma = suma + n
promedio = suma / cantidad
print("el promedio es:, {}.".format(promedio))

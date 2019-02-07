##realizar el promedio de 5notas utilizando el ciclo for

print("bienvenido al programa".center(50, "-"))

suma = 0
for i in range (5):
    nota = int(input("ingrese nota: "))
    suma = suma + nota
    promedio = suma / 5
print("el promedio es {}".format(promedio))

               

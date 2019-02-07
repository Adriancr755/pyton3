##solicitar al usuario que seleccione una ocpioc opcion 1. solicitar dos numeros y elevar el primer numero al sugundo numero opcion 2. solicitar 3 numeros
##y elebarlo al primero al segundo

elevacion = 0 
print("bienvenido al programa".center(50, "-"))
opcion=input("1.elevar dos num el primero por el segundo 2.elevar 3 numeros y elevar el primero por el segundo: ")

if opcion == "1":
    valor1 = int(input("ingrese un valor: "))
    valor2 = int(input("ingrese un valor: "))
    elevacion = valor1 ** valor2
    print ("la elevacion es {}".format(elevacion))
elif opcion == "2":
    valor1 = int(input("ingrese un valor: "))
    valor2 = int(input("ingrese un valor: "))
    valor3 = int(input("ingrese un valor: "))
    elevacion = (valor1 ** valor2) ** valor3
    print ("la elevacion es {}".format(elevacion))   
else:
    print("opcion invalida")















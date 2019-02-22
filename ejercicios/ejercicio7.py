print ("BIENVENIDO AL POGRAMA".center (50, "-"))

URGENCIAS = 0.37
PEDRIATRIA = 0.42
TRAUMATOLOGIA = 0.21
Aumento_en_area = 0

salida = input("ingresar presupuesto 1-si \ 2-no")
while salida != 2:
    presupuesto = int(input("ingresar la cantidad"))
    print("la cantidad en urgencias es:. {}".format(presupuesto * URGENCIAS))
    print("la cantidad en pedriatria es:. {}".format(presupuesto * PEDRIATRIA))
    print("la cantidad en traumatologia es:. {}".format(presupuesto * TRAUMATOLOGIA))
    



    
    
    

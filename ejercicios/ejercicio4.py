DOLARES_EUROS = 2.100
EUROS_DOLARES = 1.45
CANTIDAD = 0
TOTAL = 0

print("bienvenido al conversor".center(50, "-"))
opcion=input("1.Dolares a Euros 2.Euros a Dolares a: ")

if opcion == "1":
    Dolares = input ("cantidad en dolares: ")
    saldo = float(Dolares) / DOLARES_EUROS
    print ("la conversion es: ",saldo)
elif opcion == "2":
    Euros = input ("cantidad en Euros: ")
    saldo = float (euros) / EUROS_DOLARES
    print ("la conversion es: ",saldo)
else:
    print ("opcion invalida")
    
    

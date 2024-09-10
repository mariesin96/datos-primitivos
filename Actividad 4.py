#Definimos una variable tipo flotante
saldo = 100.0

#simulamos un ciclo de retiros de saldo hasta que el saldo sea menor que 10
while saldo > 10:
    retiro = 15.0
    saldo -= retiro
    print(f"se ha retirado {retiro}, saldo actual: {saldo}")
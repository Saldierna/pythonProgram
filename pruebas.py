import time
from random import random

print("Hola Usuario")
pin = int(input("Ingresa tu pin:  "))
saldo = int(1000)
mov = []

if pin == 1235:
    print("VALIDANDO SU PIN...")
    #time.sleep(2)
    pin = int(input("PIN CORRECTO POR SEGURIDAD, DIGITE DE NUEVO:  "))
    if pin == 1235:
        print("VALIDANDO SU PIN POR SEGUNDA VEZ...")
        #time.sleep(2)
        pin = int(input("PIN CORRECTO POR SEGURIDAD, UNA ULTIMA VEZ DIGITE DE NUEVO: "))
        if pin == 1235:
            print("VALIDANDO SU PIN POR TERCERA VEZ...")
            #time.sleep(2)
            print("..::BEVENIDO USUARIO::..")
            while True:
                eleccion = int(input("\n1)Consultar saldo\n2)Retirar saldo\n3)Historico de Movimientos\n4)Salir\n"))
                if eleccion == 1:
                     print(f"Tu saldo es: ${saldo}")
                     a = (input("\n1)Regresar al menu\n2)Salir\n"))
                     if a == "1":
                      continue
                     else:
                       break
                elif eleccion == 2:
                    if saldo > 0:
                        retiro = input("¿Cuanto quieres retirar?\n")
                        saldo = int(saldo) - int(retiro)
                        print(f"Tu saldo es ${saldo}")
                        m=mov.append(int(saldo))
                        print(m)
                        a = (input("\n1)Regresar al menu\n2)Salir\n"))
                        if a == "1":
                            continue
                        else:
                            print("Vuelva pronto")
                            break
                    elif saldo == 0:
                        print(f"No tienes fondos suficientes, tu saldo es de: ${saldo}")
                        a = (input("\n1)Regresar al menu\n2)Salir\n"))
                        if a == "1":
                            continue
                        else:
                            print("Vuelva pronto")
                            break
                    else:
                        print("No tienes salgo suficiente")
                elif eleccion == 3:
                    print(" -----------------------------------------------------------------------")
                    print("Banco Saldierna")
                    print("                                                                       ")
                    print(f"Saldo: ${saldo}")
                    print("Fecha:", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
                    print("Banco de cuenta: ****** Sucursal Londres")
                    print("      AQUI ESTA EL CAMBIO                                                     ")
                    print(" -----------------------------------------------------------------------")
                else:
                    print("HASTA LUEGO")
                    break
        else:
            time.sleep(2)
            print("PIN Incorrecto")
    else:
        time.sleep(2)
        print("PIN INCORRECTO")
else:
    time.sleep(2)
    print("PIN Incorrecto")
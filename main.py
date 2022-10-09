#MENU
import time
import sys
#VARIABLES
pin = ""
print("Bienvenido al 'BANCO SALDIERNA'")

def pin_val():
    #print("Hola Usuario")
    pin = int(input("Ingresa tu pin:  "))

    if pin == 1235:
        print("VALIDANDO SU PIN...")
        time.sleep(2)
        pin = int(input("PIN CORRECTO POR SEGURIDAD, DIGITE DE NUEVO:  "))
        if pin == 1235:
            print("VALIDANDO SU PIN POR SEGUNDA VEZ...")
            time.sleep(2)
            pin = int(input("PIN CORRECTO POR SEGURIDAD, UNA ULTIMA VEZ DIGITE DE NUEVO: "))
            if pin == 1235:
                print("VALIDANDO SU PIN POR TERCERA VEZ...")
                time.sleep(2)
                print = ("..::BEVENIDO USUARIO::..")
            else:
                time.sleep(2)
                print("PIN Incorrecto")
        else:
            time.sleep(2)
            print("PIN INCORRECTO")
    else:
        time.sleep(2)
        print("PIN Incorrecto")


def main():
    pin_val()
    #print('¿Que operacion deseas hacer?')
    eleccion = int(input("\n 1) CONSULTAR SALDO  \n 2) RETIRAR SALDO   \n 3) HISTORICO DE MOVIMIENTOS"))

if __name__ == '__main__':
    pin_val()
    # print('¿Que operacion deseas hacer?')
    eleccion = int(input("\n 1) CONSULTAR SALDO  \n 2) RETIRAR SALDO   \n 3) HISTORICO DE MOVIMIENTOS"))








# ==================================================
# =      Billetera de Criptomonedas Personal       =
# ==================================================

import os
import time
import API
import json
from datetime import date
from datetime import datetime

# variables iniciales
transaccion = {}
iden = 0
aux = 0
cantidadAnte = 0
monedas = {}
# Fecha actual
now = datetime.now()

while True:
    # opciones del menu
    print('1. Recibir cantidad')
    print('2. Transferir monto')
    print('3. Mostrar balance una moneda')
    print('4. Mostrar balance general')
    print('5. Mostrar histórico de transacciones')
    print('6. Salir del programa')
    entrada = int(input("\nIntroduzca su respuesta: "))
    if entrada <= 0 or entrada > 6:
        print("\nEntrada incorrecta")
        time.sleep(2)
        os.system("clear")
        continue

    # opcion de recibir
    if entrada == 1:
        moneda = input("Introduzca el tipo de moneda: ")
        recibir = int(input("Cantidad a recibir(Criptomoneda): "))
        codigo = input("Codigo: ")

        # verificacion de si la moneda existe
        if not API.isMoney(moneda):
            print("\nMoneda Invalida.")
            time.sleep(1)
            os.system("clear")
            continue
        else:
            # conversion de criptomoneda a USD
            recibirTransfe = recibir
            USD = API.convertir(moneda, recibir, 'USD')
            if aux != 0:
                for client in transaccion[iden]:
                    cantidadAnte = client['cantidadTotal']
                if moneda in monedas.keys():
                    recibir = monedas[moneda][0]+recibir
                    USD = monedas[moneda][1]+USD
                iden = iden+1

            monedas[moneda] = [recibir, USD]

            # almacenar el contenido que sera el historial
            transaccion[aux] = []
            transaccion[aux].append({
                'fecha': now.strftime('%x %X'),
                'moneda': moneda,
                'motivo': 'Recibir',
                'codigo': codigo,
                'cantidad': recibirTransfe,
                'cantidadTotal': recibirTransfe + cantidadAnte
            })
            aux = aux + 1
            # guardar el historial en un json
            with open('transaccion.json', 'w') as f:
                json.dump(transaccion, f)
            print("Cantidad Recibida")

    # opcion de tranferir
    elif entrada == 2:
        print("TRANSFERIR:")
        moneda = input("Introduzca el tipo de moneda: ")
        monto = int(input("Monto a enviar(USD): "))
        codigo = input("Codigo: ")

        # verificacion de si la moneda existe
        if not API.isMoney(moneda):
            print("\nMoneda Invalida.")
            time.sleep(1)
            os.system("clear")
            continue
        else:
            # conversion de USD a criptomoneda
            montoTranfe = monto
            CRIPTO = API.convertir(moneda, monto, 'cripto')
            if aux != 0:
                for client in transaccion[iden]:
                    cantidadAnte = client['cantidadTotal']
                if moneda in monedas.keys():
                    CRIPTO = monedas[moneda][0]-CRIPTO
                    monto = monedas[moneda][1]-monto
                iden = iden+1

            monedas[moneda] = [CRIPTO, monto]

            # almacenar el contenido que sera el historial
            transaccion[aux] = []
            transaccion[aux].append({
                'fecha': now.strftime('%x %X'),
                'moneda': moneda,
                'motivo': 'Transferir',
                'codigo': codigo,
                'cantidad': montoTranfe,
                'cantidadTotal': montoTranfe - cantidadAnte
            })
            aux = aux + 1
            # guardar el historial en un json
            with open('transaccion.json', 'w') as f:
                json.dump(transaccion, f)
            print("Transferencia completada")

    # opcion de balance de moneda
    elif entrada == 3:
        print('BALANCE DE UNA MONEDA:')
        cry = input("Introduzca la moneda: ")

        # mostrar el balance segun la moneda solicitada
        if cry in monedas:
            print("Moneda: ", cry, " Cantidad(CRY): ",
                  monedas[cry][0], " USD: ", monedas[cry][1])
        else:
            print("Monedas no encontrada")

    # opcion de balance general
    elif entrada == 4:
        if len(monedas) == 0:
            print("Aun no hizo transacciones")
        else:
            print('BALANCE GENERAL:')
            usdTotal = 0
            # mostrar todos los balances de cada moneda
            for x in monedas:
                usdTotal += monedas[x][1]
                print("Moneda: ", x, " Cantidad(CRY): ",
                      monedas[x][0], " USD: ", monedas[x][1])

            print('USD Total de todas las monedas: ', usdTotal)

    # opcion de historia de transacciones
    elif entrada == 5:
        if len(transaccion) == 0:
            print('Todavia no hay historial de transacciones')
        else:
            print('HISTORIAL DE TRANSACCIONES:')
            a = 0
            # recorrer el json y mostrar el historial de transaccion
            while a < len(transaccion):
                for cliente in transaccion[a]:
                    print(a, ' Fecha: ', cliente['fecha'], ' Moneda: ', cliente['moneda'], ' Motivo: ', cliente['motivo'], ' Codigo: ',
                          cliente['codigo'], ' Cantidad: ', cliente['cantidad'], ' Cantidad Total: ', cliente['cantidadTotal'])
                a = a+1
    # opcion salir
    elif entrada == 6:
        break
    cantidadAnte = 0
    time.sleep(5)
    os.system("clear")

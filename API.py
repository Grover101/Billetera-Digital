import requests
import json

# si la llave no funcion, recomiendo que solicite un llave a https://pro.coinmarketcap.com/account
key = '8a7aa22e-2f96-4a6e-aeb6-6bdf74be4a40'

# funcion de datos requeridos por la api


def api(cripto):
    # los datos que la api requiere
    headers = {'Accepts': 'application/json',  'X-CMC_PRO_API_KEY': key}
    # los parametros que requiere la api
    parametros = {'symbol': cripto}
    # solicitando a la api, retorna un json
    return requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest", headers=headers, params=parametros, timeout=1).json()

#  verificar si existe la moneda solicitada


def isMoney(cripto):
    data = api(cripto)
    try:
        # retorna la mondeda existente
        return cripto in data['data']
    except:
        # en caso que la moneda no existe
        return False

# convertir una criptomoneda a USD y vicervesa


def convertir(cripto, cantidad, cambio):
    if cambio == 'USD':
        # solicita la criptomoneda
        data = api(cripto)
        # el valor de USD de la criptomoneda
        precioUSD = data['data'][cripto]['quote']['USD']['price']
        # retorna el equivalente a la cantidad
        return cantidad * precioUSD
    elif cambio == 'cripto':
        # solicita la criptomoneda
        data = api(cripto)
        # el valor de la criptomoneda en USD
        precioCRIPTO = data['data'][cripto]['quote']['USD']['price']
        # retorna el equivalente a la cantidad
        return cantidad / precioCRIPTO

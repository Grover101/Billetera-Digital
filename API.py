import requests
import json

# la llave es temporal si quieres probarlo solicita un llave a coinmarketcap.com
key = '2448e9c9-b938-4f0e-85f1-9878a7b41c87'

# funcion de datos requeridos por la api
def api(cripto):
	# los datos que la api requiere
	headers = {  'Accepts': 'application/json',  'X-CMC_PRO_API_KEY': key }
	# los parametros que requiere la api
	parametros = {'symbol': cripto}
	# solicitando a la api, retorna un json 
	return requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest",headers=headers,params=parametros).json()

#  verificar si existe la moneda solicitada
def isMoney():
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
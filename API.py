import requests
import json

def api(cripto):
	# los datos que la api requiere
	headers = {  'Accepts': 'application/json',  'X-CMC_PRO_API_KEY':  '2448e9c9-b938-4f0e-85f1-9878a7b41c87'}
	# los parametros que requiere la api
	parametros = {'symbol': cripto}
	# solicitando a la api, retorna un json 
	return requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest",headers=headers,params=parametros).json()
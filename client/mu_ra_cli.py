############################################
#
#   Client rest api to write markupdate data
#
############################################

import requests, logging, json
import pandas as pd


def mu_put_log(pl, rx, pk_flag):
	logger.info('Payload: ')
	logger.info(pl)
	logger.info('Put requested: ' + rx.url) 
	logger.info('Status code: ' + str(rx.status_code)) 
	logger.info('Response header:' +  str(rx.headers))

	response_content = rx.json()

	response_pk = -1
	if pk_flag:
		response_pk = response_content['pk']

	logger.info('Content response:' +  str(response_content))
	logger.info('Content pk value:' + str(response_pk))
	return response_pk


###############################################
#   Set logging 
###############################################
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
# create a file handler
handler = logging.FileHandler('mu_ra_cli.log')
handler.setLevel(logging.INFO)
# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(handler)

logger.info('Logging started')


###############################################
#   Read parms: HOST:PORT 
###############################################
f=open('mu_ra_cli.json', encoding = 'UTF-8')
parms_lines =  [json.loads(line) for line in f.read().splitlines()]
for parms in parms_lines:
	Host = parms["Host"]
	XLSFile = parms["XLSFile"]
	XLSSheet = parms["XLSSheet"]


###############################################
#  Write marke data
#  1. update
#  2. categories
#  3. symbols 
#  4. values
################################################
market_data = pd.read_excel(XLSFile, XLSSheet)
URL_UPDATE = 'updates/'
URL_CATEGORY = 'categories/'
URL_SYMBOL = 'symbols/'
URL_VALUES = 'values/'
THIS_UNIT = {'%':1, 'bps':2, 'ticks':3, '':4, '€':5, 'pts':6}


# Update
ts = market_data.loc[0]['Value']
update_date = str(ts.date())
update_time = str(ts.time())
update_des = market_data.loc[0]['Description']

#update_hook = update_time + '@' + update_time
payload_update = {'notes_text': 'rilevazione di prova da client', 'pub_date': update_date, 'pub_hour': update_time}

#cleaning dataframe
mudata = market_data[market_data['Value'].isnull() != True]
mudata = mudata.drop(mudata.index[0])

last_category = ''
last_symbol = ''


try:

	#insert update record
	r = requests.post(Host + URL_UPDATE, data = payload_update)
	#log it
	update_pk = mu_put_log(payload_update, r, True)

	#loop over mudata
	for index, row in mudata.iterrows() :

	    #category flow
	    if (row['Topic'] != last_category) :
	    	payload_category = { "name": 'Topic', "description": row['Topic'][:min(len(row['Topic']),200)],	"update": update_pk}
	    	r = requests.post(Host + URL_CATEGORY, data = payload_category)
	    	category_pk = mu_put_log(payload_category, r, True)

	    #symbol flow
	    if (row['Ticker'] != last_symbol) :
	    	payload_symbol = { "name": "Ticker", "description":	row['Ticker'][:min(len(row['Ticker']),200)], "category": category_pk }
	    	r = requests.post(Host + URL_SYMBOL, data = payload_symbol)
	    	symbol_pk = mu_put_log(payload_symbol, r, True)

	    #value flow
	    payload_value = { "value": row['Value'], "unit": THIS_UNIT[row['Unit']], "precision": int(row['Precision']), "val_format": int(row['Format']), "val_sequence": int(row['Sequence']), "description":  row['Description'][:min(len(row['Description']),200)], "symbol": symbol_pk }
	    r = requests.post(Host + URL_VALUES, data = payload_value)
	    value_pk = mu_put_log(payload_value, r, False)
	    #broken code technique flow
	    last_category = row['Topic']
	    last_symbol = row['Ticker']

except:
	logger.error('An error occurred')
	raise




#urls_category = 'api/categories/'
#payload_category = {'name': 'Titoli gevernativi', 'description': 'Tassi e Spread principali titoli benchmark', 'update': update_pk}
#r = requests.post(Host + urls_category, data = payload_category)
#print('URL request' + r.url)
#print('Request status code: ' + str(r.status_code))

#payload_category = {'name': 'Tassi', 'description': 'Principali punti della curva EUR IRS', 'update': update_hook}
#r = requests.post(Host + urls_category, data = payload_category)
#print('URL request' + r.url)
#print('Request status code: ' + str(r.status_code))


#urls_symbol = 'api/symbol/'
#payload_symbol = {'notes_text': 'rilevazione di prova da client', 'pub_date': '2018-08-03', 'pub_hour': '08:00:00'}
#r = requests.post(Host + urls_symbol, data = payload_symbol)
#print('URL request' + r.url
#print('Request status code: ' + str(r.status_code))

#urls_value = 'api/value/'
#payload_value = {'notes_text': 'rilevazione di prova da client', 'pub_date': '2018-08-03', 'pub_hour': '08:00:00'}
#r = requests.post(Host + urls_value, data = payload_value)
#print('URL request' + r.url)
#print('Request status code: ' + str(r.status_code))

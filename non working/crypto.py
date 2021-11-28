
from requests import Request, Session

from tkinter import *
import json
import pprint

url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"






#### for tk window
 
parameters = {
	
	'slug':'bitcoin',
	'convert':'USD' 
        
}

headers = {
	'Accepts':'application/json',
	'X-CMC_PRO_API_KEY':'0cfc20b1-a98d-4314-92c4-71bc5757f57d'

}



session = Session()
session.headers.update(headers)

response = session.get(url, params=parameters)

### to get the json data from BTC


print("BITCOIN")
# #gives out more json information 
#pprint.pprint(json.loads(response.text)['data'])
pprint.pprint(json.loads(response.text)['data']['1']['quote']['USD']['price'])
#json loads put its in json format instead of string
#pprint is inbuilt python library




parameters = {

     'slug':'dogecoin',
     'convert':'USD'

}

headers = {
	'Accepts':'application/json',
	'X-CMC_PRO_API_KEY':'0cfc20b1-a98d-4314-92c4-71bc5757f57d'

}

sessiondoge = Session()
sessiondoge.headers.update(headers)
response = sessiondoge.get(url,params=parameters)
print("DOGECOIN")
pprint.pprint(json.loads(response.text)['data'])


parameters = {

     'slug':'ravencoin',
     'convert':'USD'

}

headers = {
	'Accepts':'application/json',
	'X-CMC_PRO_API_KEY':'0cfc20b1-a98d-4314-92c4-71bc5757f57d'
}

sessionrvn = Session()
sessionrvn.headers.update(headers)
response = sessionrvn.get(url,params=parameters)
print("RAVENCOIN")
pprint.pprint(json.loads(response.text)['data'])
  
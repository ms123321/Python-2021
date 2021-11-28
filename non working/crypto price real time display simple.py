import kivy
from requests import Request, Session
from time import sleep
from tkinter import *
import json
import pprint



url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"


      



#### bitcoin############
 
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

#pprint.pprint(json.loads(response.text)['data'])
# #gives out more json information 
pprint.pprint(json.loads(response.text)['data']['1']['quote']['USD']['price'])
#json loads put its in json format instead of string
#pprint is inbuilt python library


########Litecoin###############

parameters = {

     'slug':'litecoin',
     'convert':'USD'

}

headers = {
	'Accepts':'application/json',
	'X-CMC_PRO_API_KEY':'0cfc20b1-a98d-4314-92c4-71bc5757f57d'

}

sessionLTC = Session()
sessionLTC.headers.update(headers)
response = sessionLTC.get(url,params=parameters)
print("LITECOIN")
pprint.pprint(json.loads(response.text)['data']['2']['quote']['USD']['price'])


######dogecoin#####################

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
pprint.pprint(json.loads(response.text)['data']['74']['quote']['USD']['price'])

########### ravencoin####################
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
pprint.pprint(json.loads(response.text)['data']['2577']['quote']['USD']['price'])





 



#####################################################################################################################################






####example of how to add , you need the special number so do
#pprint.pprint(json.loads(response.text)['data']) --- FIRST do that one first below to find the keypairs 
'''
parameters = {

     'slug':'YOURCOINAMEHERE',
     'convert':'USD'

}

headers = {
	'Accepts':'application/json',
	'X-CMC_PRO_API_KEY':'0cfc20b1-a98d-4314-92c4-71bc5757f57d'
}

sessionVARIABLE = Session()
sessionVARIABLE.headers.update(headers)
response = sessionVARIABLE.get(url,params=parameters)
print("RAVENCOIN")
pprint.pprint(json.loads(response.text)['data']['2577']['quote']['USD']['price'])

############################
#cryptos to add - ones you buy? 
#ontology
#ark
#ontology gas
#stormx?
#function x 

'''
window.mainloop()


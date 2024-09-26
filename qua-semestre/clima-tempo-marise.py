import requests
import json

def lambda_handler(event, context):

    iTOKEN = event['token'],

    # aqui vc associa o tipo de consulta 1 para pegar o ID da cidade no Portal Climatempo e tipo 2 traz o json com todos os dados do clima relattivo ao ID da Cidade\n",
    iTIPOCONSULTA = 2

    if iTIPOCONSULTA == 1:
        iCITY = event['cidade']
        iURL = (f"http://apiadvisor.climatempo.com.br/api/v1/locale/city?name={iCITY}&token={str(iTOKEN)}")
        iRESPONSE = requests.request("GET",iURL)
        iRETORNO_REQ = json.loads(iRESPONSE.text)

        print(iRETORNO_REQ)
        print(iURL)
        # for iCHAVE in iRETORNO_REQ:
        #     iID = iCHAVE['id']
        #     iNAME = iCHAVE['name']
        #     iSTATE = iCHAVE['state']
        #     iCOUNTRY = iCHAVE['country']
        #     print("id:" + str(iID) + " idiNAME:" + str(iNAME) + "iSTATE:" + str(iSTATE) + " iCOUNTRY" + str(iCOUNTRY))
        #     iNEWCITY = input("Informe o ID da cidade")
        #     iURL = "http://apiadvisor.climatempo.com.br/api-manager/user-token/" + str(iTOKEN) + "/locales",
        #     payload = "localeId[]=" + str(iNEWCITY)
        #     headers = {'Content-Type':'application/x-www-form-urlencoded'}
        #     iRESPONSE = requests.request("PUT", iURL, data=payload, headers=headers)
        #     #iRETORNO_REQ = json.loads(iRESPONSE.text)\n",
        #     #print(iRETORNO_REQ)\n",
        #     print(iRESPONSE)
            
            # até aqui a requisição deu certo por ID de cidade. A partir dai, fazer a consulta via token user para obter o json : 'id': 7564, 'name': 'Salvador', 'state': 'BA', 'country': 'BR', 'data': {'temperature': 28, 'wind_direction': 'E', 'wind_velocity': 4, 'humidity': 62, 'condition': 'Sol', 'pressure': 1015, 'icon': '1', 'sensation': 29, 'date': '2024-06-21 15:11:43'}}\n",
            # http://apiadvisor.climatempo.com.br/api/v1/climate/rain/locale/3477?token=your-app-token\n",
            
    if iTIPOCONSULTA == 2:
        iURL = (f"http://apiadvisor.climatempo.com.br/api/v1/weather/locale/{event['id']}/current?token=09e05f37e474a9f8f676b75b50988765")
        iRESPONSE = requests.request("GET", iURL)
        iRETORNO_REQ = json.loads(iRESPONSE. text)
        print(iRETORNO_REQ)

lambda_handler({"id"})
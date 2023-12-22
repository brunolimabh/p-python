import requests 
import json

mensagem = {"text": f"""
    🚨ALERTA🚨

Descrição  => Sua CPU ultrapassou 95%!   
"""}
chatBanco = "https://hooks.slack.com/services/XPTO"

postMsg = requests.post(chatBanco, data=json.dumps(mensagem))
print(postMsg.status_code)




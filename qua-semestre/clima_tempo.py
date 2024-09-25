import requests
import json

def lambda_handler(event, context):
    try:
        url = "http://apiadvisor.climatempo.com.br/api/v1/anl/synoptic/locale/BR?token=" + event["token"]
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            
            print(data)
            return True
        else:
            print(f"Erro: {response.status_code}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Erro: {e}")
        return None



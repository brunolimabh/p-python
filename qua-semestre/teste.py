import json
import requests
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    url = "https://olinda.bcb.gov.br/olinda/servico/Pix_DadosAbertos/versao/v1/odata/EstatisticasTransacoesPix(Database=@Database)?@Database='202011'&$top=100&$format=json"

    try:
        resultado = requests.get(url)
        # Verifica se a requisição foi bem-sucedida
        resultado.raise_for_status()
        # Decodifica o JSON
        dados = resultado.json()
        
        # Extrai a lista de transações Pix
        transacoes = dados['value']
        
        bucket_name = event['bucket']
        file_name = 'pix.json'
        json_data = json.dumps(transacoes)

        s3.put_object(
            Bucket=bucket_name,
            Key=file_name,
            Body=json_data,
            ContentType='application/json')
        
        print("JSON gravado no S3 com sucesso")
        
        return True
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar JSON: {e}")
        print(f"Resposta completa da API: {resultado.text}")
        return None

print(lambda_handler({"bucket": "pix-s3" }, None))
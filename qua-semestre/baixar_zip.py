import requests
import zipfile as zp
import os

CSV_URL = "https://www.justicaeleitoral.jus.br/arquivos/tse-anexo-massa-de-teste-2017"

def lambda_handler(event, context):
    try:
        with requests.Session() as s:
            download = s.get(CSV_URL)

            if download.status_code == 200:
                zip_path = '/tmp/TSE-anexo-massa-teste-2017.zip'

                with open(zip_path, 'wb') as file:
                    file.write(download.content)

                extracted_folder = "/tmp/dados"
                with zp.ZipFile(zip_path, 'r') as zip_ref:
                    zip_ref.extractall(extracted_folder)

                extracted_file_path = os.path.join(extracted_folder, "folha.txt")
                if os.path.exists(extracted_file_path):
                    with open(extracted_file_path, 'r', encoding='latin-1') as folha:
                        return folha.read()
                else:
                    print("arquivo não encontrado")
                    return None
            else:
                print(f"erro ao baixar o arquivo")
                return None

    except requests.exceptions.RequestException as e:
        print(f"erro: {e}")
        return None
    except zp.BadZipFile as e:
        print(f"erro ao abrir o zip: {e}")
        return None
    except UnicodeDecodeError as e:
        print(f"erro ao ler o arquivo: {e}")
        return None

print(lambda_handler(None, None))

import csv
import requests

CSV_URL = "https://servicos.dpf.gov.br/dadosabertos/SINARM/OCORRENCIAS/SINARM_OCORRENCIAS_MUINICIPIOS_MENOS_100MIL_HABITANTES.csv"


with requests.Session() as s:
    download = s.get(CSV_URL)
    with open('SINARM_OCORRENCIAS_MUINICIPIOS_MENOS_100MIL_HABITANTES.csv', 'wb') as open2023:
        open2023.write(download.content)
        with open(("SINARM_OCORRENCIAS_MUINICIPIOS_MENOS_100MIL_HABITANTES.csv")) as f:
                file_content=f.read()
                cr = csv.reader(file_content.splitlines(), delimiter=';')
                my_list = list(cr)
                # print(my_list)

arquivo = "C:/Users/bruno/Documents/projetosPy/crawler/ocorrencias-roubos-furtos/ocorrencias.csv"
with open(arquivo, mode='w', newline='') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)
        escritor_csv.writerow(["ANO", "MES","UF","ARMA","MARCA","CALIBRE","TIPO", "TOTAL"])

        for row in my_list:
            if(row[0] == "2023") and (row[1] == "10"):
                escritor_csv.writerow([row[0],row[1],row[2],row[3].strip(),row[4].strip(),row[5].strip(),row[6].strip(),row[7]])
                arquivo_csv.flush()
                with open(arquivo, mode='r') as arquivo_leitura:
                    conteudo = arquivo_leitura.read()
                print("Conteúdo do arquivo CSV:")
                print(row[0],row[1])


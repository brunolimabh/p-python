import psutil
from datetime import datetime
import mysql.connector
import platform
import time
 
conexao = mysql.connector.connect(user='xpto', password='xpto', host='xpto', database='xpto')

cursor = conexao.cursor()

def rudge_ramos():
    cont = 0
    
    qtd_core = psutil.cpu_count(logical=False)
    cpu_um_speed_max = psutil.cpu_freq().max / pow(10,3)
    ram_um_total = (psutil.virtual_memory().total) / pow(10,9)
    so = platform.system()
    if (so == 'Windows'):
        disco_um_total = psutil.disk_usage('C:\\').total / pow(10,9)
    elif (so == 'Linux'):
        disco_um_total = psutil.disk_usage('/bin').total / pow(10,9)
    
    while True:
        data = datetime.now()
        data = data.strftime('%Y/%m/%d %H:%M:%S')
        cpu_m1 = psutil.cpu_percent(interval=1)
        cpu_m1_speed = psutil.cpu_freq().current / pow(10,3)
        ram_m1_used = (psutil.virtual_memory().used) / pow(10,9)
        ram_m1 = psutil.virtual_memory().percent
        if (so == 'Windows'):
            disco_m1 = psutil.disk_usage('C:\\').percent
        elif (so == 'Linux'):
            disco_m1 = psutil.disk_usage('/bin').percent
        
        cursor.execute(f"INSERT INTO Registro (valor, dataHora, fkComponente, fkTotem) VALUES ({cpu_m1}, NOW(), 1, 1), ({ram_m1}, NOW(), 2, 1),({disco_m1}, NOW(), 3, 1);")
            
        conexao.commit()
        cont+=1
        print(cont)
        # time.sleep(1)
 
if (conexao.is_connected()):
    print("A Conexão ao MySql foi iniciada ")
    rudge_ramos()
else:
    print("Houve erro ao conectar")
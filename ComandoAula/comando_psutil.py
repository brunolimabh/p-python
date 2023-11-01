import psutil
import time 
import mysql.connector
from datetime import datetime

mydb = mysql.connector.connect(
  host="xpto",
  user="xpto",
  password="xpto",
  database="xpto"
)


while True:
    
    data = datetime.now()
    data = data.strftime('%d/%m/%Y %H:%M:%S')

    user = [user[0] for user in psutil.users()]
    user = user[0]
    processador = "não sei"
    qtd_core = psutil.cpu_count(logical=False)

    cpu_porcent = psutil.cpu_percent(interval=1)
    cpu_speed = psutil.cpu_freq().current / 1000
    cpu_speed_max = psutil.cpu_freq().max / 1000

    disc_total = psutil.disk_usage('C:\\').total / 1000000000
    disc_used = psutil.disk_usage('C:\\').used / 1000000000
    disc_percent = psutil.disk_usage('C:\\').percent

    ram_total = (psutil.virtual_memory().total) / 1000000000
    ram_used = (psutil.virtual_memory().used) / 1000000000
    ram_percent = psutil.virtual_memory().percent

    msgOpen = f"""
     __________________________________________________________________
    |                                                                  |
    | Bank Secure Monitor Report               {data:10s}     |
    | _________________________________________________________________|
    |                                                                  |
    | USER ==> {user:20s}                                    |
    |__________________________________________________________________|                                                                                    
    |                                                                  |
    | HARDWARE   ==> {processador:17s}                                 |
    | COREs      ==> {qtd_core:16.0f}                                  |
    |__________________________________________________________________|
    |                                                                  |
    | #          ==>     PORCENT     |      SPEED     |   MAX SPEED    |
    | CPU        ==>     {cpu_porcent:6.1f}%     |    {cpu_speed:3.2f}GHz     |   {cpu_speed_max:6.2f}GHz    |
    |__________________________________________________________________|
    |                                                                  |
    | #          ==>     PORCENT     |      TOTAL     |      USED      |
    | DISC (GB)  ==>     {disc_percent:6.1f}%     |     {disc_total:6.1f}     |    {disc_used:6.1f}      |
    | RAM  (GB)  ==>     {ram_percent:6.1f}%     |     {ram_total:6.1f}     |    {ram_used:6.1f}      |
    |__________________________________________________________________|
   
    """

    print(msgOpen)
    time.sleep(3)

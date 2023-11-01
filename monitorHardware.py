import psutil
import time 
from tkinter import *
from datetime import datetime
import os
import mysql.connector
import requests 
import json
import platform
 
conexao = mysql.connector.connect(user='xpto', password='xpto', host='xpto', database='xpto', auth_plugin = 'mysql_native_password')

cursor = conexao.cursor()

if (conexao.is_connected()):
        print("A Conexão ao MySql foi iniciada ")
else:
     print("Houve erro ao conectar")

def pegar_dados():
  
    exibiu = False
    cont = 0

    while cont <= 200:
    
     cont = cont + 1;
     data = datetime.now()
     data = data.strftime('%Y/%m/%d %H:%M:%S')

     user = [user[0] for user in psutil.users()]
     user = user[0]
     qtd_core = psutil.cpu_count(logical=False)

     cpu_porcent = psutil.cpu_percent(interval=1)
     cpu_speed = psutil.cpu_freq().current / pow(10,3)
     cpu_speed_max = psutil.cpu_freq().max / pow(10,3)

     so = platform.system()
     processor = platform.processor()

     if (so == 'Windows'):
    # DIRETÓRIO PARA WINDOWS

         disc_total = psutil.disk_usage('C:\\').total / pow(10,9)
         disc_used = psutil.disk_usage('C:\\').used / pow(10,9)
         disc_percent = psutil.disk_usage('C:\\').percent
     elif (so == 'Linux'):
    # DIRETÓRIO PARA LINUX
         disc_total = psutil.disk_usage('/bin').total / pow(10,9)
         disc_used = psutil.disk_usage('/bin').used / pow(10,9)
         disc_percent = psutil.disk_usage('/bin').percent

     ram_total = (psutil.virtual_memory().total) / pow(10,9)
     ram_used = (psutil.virtual_memory().used) / pow(10,9)
     ram_percent = psutil.virtual_memory().percent

     msgOpen = f"""
    
     Bank Secure Monitor Report               {data}     
                                                                 
     USER  ==> {user}                                                               
     SO ==> {so}                         
     COREs ==> {qtd_core}        

    
     #          ==>     PORCENT     |      SPEED     |   MAX SPEED    |
     CPU        ==>     {cpu_porcent:6.1f}%     |    {cpu_speed:3.2f}GHz     |   {cpu_speed_max:6.2f}GHz |
    
     #          ==>     PORCENT     |      TOTAL     |      USED      |
     DISC (GB)  ==>     {disc_percent:6.1f}%     |     {disc_total:6.1f}     |    {disc_used:6.1f}       |
     RAM  (GB)  ==>     {ram_percent:6.1f}%     |     {ram_total:6.1f}       |    {ram_used:6.1f}        |
   
    """
    
     comp1 = "Memória"
     comp2 = "CPU"
     comp3 = "Disco"
     cursor.execute(f"CALL inserirDadosMaquina ('{user}', '{comp1}', {ram_percent:.2f}, '{comp2}', {cpu_porcent}, '{comp3}', {disc_percent}, NOW());")

    #Gravar os dados na tabela definitiva
     conexao.commit()
     texto_cotacao['text'] = msgOpen
     janela.update()
    #  time.sleep(3)

     
# cria a janela
janela = Tk()
janela.title("Seja bem-vindo(a!)")
janela.geometry("2000x800")
janela.config(bg="#212529")

# qual janela ele faz parte e qual é o texto
texto_dados = Label(janela, bg="#47b2e4",fg="#000", height = 30, width = 50) 
texto_dados.place(x=620, y= 70)

texto_dados2 = Label(janela, text="Clique aqui para ver os registros da Cpu, disco e memória" )
texto_dados2.place(x=640, y= 95)

#passar a função como parametro, não estou executando a função
botao = Button(janela, text="Buscar dados", command=pegar_dados)
botao.place(x=750, y= 170)

texto_cotacao= Label(janela, text="")
texto_cotacao.pack(ipadx=10, ipady=10, padx=3, pady=250)
texto_cotacao.place(x=630, y=250)

# caminho da imagem
pastaApp = os.path.dirname(__file__)

# para deixar a janela exibida
janela.mainloop()

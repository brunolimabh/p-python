# Importando as bibliotecas necesárias para tratar os datos, e destacando o zipfile para descompactar arquivos zipados
import csv
import requests
import zipfile as zp
from tkinter import *
import tkinter as tk

CSV_URL="https://portal.inmet.gov.br/uploads/dadoshistoricos/2023.zip"

json = 0;

# Acessando o link do download, descompactando o arquivo e atribuindo o nome de "dados2023", e abrindo um csv especifico de uma cidade, dourados
with requests.Session() as s:
    download = s.get(CSV_URL)
    with open('2023.zip', 'wb') as open2023:
        open2023.write(download.content)
        with zp.ZipFile('2023.zip', 'r') as desc2023:
            desc2023.extractall("dados2023")
            with open(("dados2023/INMET_CO_MS_A721_DOURADOS_01-01-2023_A_30-09-2023.CSV")) as f:
                file_content=f.read()
                cr = csv.reader(file_content.splitlines(), delimiter=';')
                my_list = list(cr)
                json = my_list


for row in my_list:
    print(row)

lista01 = []
lista02 = []
lista03 = []
lista04 = []

# Pegando todos os dados de temperatura nos dias 1 a 4 do mes de outrubro da cidade de dourados e tratando os dados, convertendo os para numérico
for row in my_list:
    if (row[0] == "2023/09/01"):
        num = float(row[7].replace(",","."))
        lista01.append(num)
    if (row[0] == "2023/09/02"):
        num = float(row[7].replace(",","."))
        lista02.append(num)
    if (row[0] == "2023/09/03"):
        num = float(row[7].replace(",","."))
        lista03.append(num)
    if (row[0] == "2023/09/04"):
        num = float(row[7].replace(",","."))
        lista04.append(num)

# ordenando a lista dos dados para melhor manipulacao
lista01.sort()
lista02.sort()
lista03.sort()
lista04.sort()

print(lista01)
print(lista02)
print(lista03)
print(lista04)
    
root = Tk()

# menu aonde o usuario pode selecionar qual data ele deseja visualizar as metricas de temperatura
def principal():
    root.title("Clima Tempo Dourados - MS")
    root.configure(background="#12898A")
    root.geometry("300x200")
    root.resizable(False, False)
    
    frame1 = Frame(root, border=4, bg= "#0C5765", highlightbackground="black",highlightthickness=2)
    frame1.place(relx= 0.1,rely= 0.15, relwidth=0.8, relheight= 0.3)

    frame2 = Frame(root, border=4, bg= "#0C5765", highlightbackground="black",highlightthickness=2)
    frame2.place(relx= 0.1,rely= 0.55, relwidth=0.8, relheight= 0.3)

    bt1 = Button(frame1, text="DIA 1", command=DIA1, bg="#DCDCDA")
    bt1.place(relx=0.05,rely=0.2, relwidth=0.15, relheight= 0.6)
    bt2 = Button(frame1, text="DIA 2", command=DIA2, bg="#DCDCDA")
    bt2.place(relx=0.30,rely=0.2, relwidth=0.15, relheight= 0.6)
    bt3 = Button(frame1, text="DIA 3", command=DIA3, bg="#DCDCDA")
    bt3.place(relx=0.55,rely=0.2, relwidth=0.15, relheight= 0.6)
    bt4 = Button(frame1, text="DIA 4", command=DIA4, bg="#DCDCDA")
    bt4.place(relx=0.80,rely=0.2, relwidth=0.15, relheight= 0.6)
        
    root.mainloop()


def DIA1():
    tela = tk.Toplevel()
    tela.title("DIA 1")
    tela.configure(background="#DCDCDA")
    tela.geometry("350x300")
    tela.resizable(False, False)

# calculando a media da tempertaura e exindo a temp max e minima
    media01 = 0
    for i in lista01:
        media01 += i   
        
    msgInfos = f"""
    Média: {media01 / len(lista01)}
    Max: {lista01[len(lista01) - 1]}
    Mínima: {lista01[0]}
    """
    
    label_usuario = Label(tela, border=4, bg= "#C2C2C2", highlightbackground="black",highlightthickness=1, text="Métricas DIA 1", anchor=W, justify=LEFT)
    label_usuario.place(relx= 0.05,rely= 0.05, relwidth=0.5, relheight= 0.1, anchor=NW)

    label_disco_ram = Label(tela, border=4, bg= "#C2C2C2", highlightbackground="black",highlightthickness=1, text=msgInfos, anchor= NW, justify=LEFT)
    label_disco_ram.place(relx= 0.05,rely= 0.8, relwidth=0.9, relheight= 0.3, anchor=W)
    

def DIA2():
    tela = tk.Toplevel()
    tela.title("DIA 2")
    tela.configure(background="#DCDCDA")
    tela.geometry("350x300")
    tela.resizable(False, False)

    media02 = 0
    for i in lista02:
        media02 += i   
        
    msgInfos = f"""
    Média: {media02 / len(lista02)}
    Max: {lista02[len(lista02) - 1]}
    Mínima: {lista02[0]}
    """
    
    label_usuario = Label(tela, border=4, bg= "#C2C2C2", highlightbackground="black",highlightthickness=1, text="Métricas DIA 2", anchor=W, justify=LEFT)
    label_usuario.place(relx= 0.05,rely= 0.05, relwidth=0.5, relheight= 0.1, anchor=NW)

    label_disco_ram = Label(tela, border=4, bg= "#C2C2C2", highlightbackground="black",highlightthickness=1, text=msgInfos, anchor= NW, justify=LEFT)
    label_disco_ram.place(relx= 0.05,rely= 0.8, relwidth=0.9, relheight= 0.3, anchor=W)

def DIA3():
    tela = tk.Toplevel()
    tela.title("DIA 3")
    tela.configure(background="#DCDCDA")
    tela.geometry("350x300")
    tela.resizable(False, False)

    media03 = 0
    for i in lista03:
        media03 += i   
  

    msgInfos = f"""
    Média: {media03 / len(lista03)}
    Max: {lista03[len(lista03) - 1]}
    Mínima: {lista03[0]}
    """

    label_usuario = Label(tela, border=4, bg= "#C2C2C2", highlightbackground="black",highlightthickness=1, text="Métricas DIA 3", anchor=W, justify=LEFT)
    label_usuario.place(relx= 0.05,rely= 0.05, relwidth=0.5, relheight= 0.1, anchor=NW)

    label_disco_ram = Label(tela, border=4, bg= "#C2C2C2", highlightbackground="black",highlightthickness=1, text=msgInfos, anchor= NW, justify=LEFT)
    label_disco_ram.place(relx= 0.05,rely= 0.8, relwidth=0.9, relheight= 0.3, anchor=W)

def DIA4():
    tela = tk.Toplevel()
    tela.title("DIA 4")
    tela.configure(background="#DCDCDA")
    tela.geometry("350x300")
    tela.resizable(False, False)

    media04 = 0
    for i in lista04:
        media04 += i   

    msgInfos = f"""
    Média: {media04 / len(lista04)}
    Max: {lista04[len(lista04) - 1]}
    Mínima: {lista04[0]}
    """

    label_usuario = Label(tela, border=4, bg= "#C2C2C2", highlightbackground="black",highlightthickness=1, text="Métricas DIA 4", anchor=W, justify=LEFT)
    label_usuario.place(relx= 0.05,rely= 0.05, relwidth=0.5, relheight= 0.1, anchor=NW)

    label_disco_ram = Label(tela, border=4, bg= "#C2C2C2", highlightbackground="black",highlightthickness=1, text=msgInfos, anchor= NW, justify=LEFT)
    label_disco_ram.place(relx= 0.05,rely= 0.8, relwidth=0.9, relheight= 0.3, anchor=W)


principal()


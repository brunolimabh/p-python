from tkinter import *
import tkinter as tk
import psutil
from datetime import datetime
import platform

root = Tk()

def principal():
    root.title("Agencia Itau Paulista")
    root.configure(background="#12898A")
    root.geometry("300x200")
    root.resizable(False, False)
    
    frame1 = Frame(root, border=4, bg= "#0C5765", highlightbackground="black",highlightthickness=2)
    frame1.place(relx= 0.1,rely= 0.15, relwidth=0.8, relheight= 0.3)

    frame2 = Frame(root, border=4, bg= "#0C5765", highlightbackground="black",highlightthickness=2)
    frame2.place(relx= 0.1,rely= 0.55, relwidth=0.8, relheight= 0.3)

    bt1 = Button(frame1, text="SI-1", command=SI1, bg="#DCDCDA")
    bt1.place(relx=0.05,rely=0.2, relwidth=0.15, relheight= 0.6)
    bt2 = Button(frame1, text="MI-1", command=MI1, bg="#DCDCDA")
    bt2.place(relx=0.30,rely=0.2, relwidth=0.15, relheight= 0.6)
    bt3 = Button(frame1, text="MI-2", command=MI2, bg="#DCDCDA")
    bt3.place(relx=0.55,rely=0.2, relwidth=0.15, relheight= 0.6)
    bt4 = Button(frame1, text="MI-3", command=MI3, bg="#DCDCDA")
    bt4.place(relx=0.80,rely=0.2, relwidth=0.15, relheight= 0.6)
        
    root.mainloop()


data = datetime.now()
data = data.strftime('%Y/%m/%d %H:%M:%S')

user = [user[0] for user in psutil.users()]
user = user[0]

qtd_core = psutil.cpu_count(logical=False)

cpu_porcent = psutil.cpu_percent(interval=1)
cpu_speed = psutil.cpu_freq().current / pow(10,3)
cpu_speed_max = psutil.cpu_freq().max / pow(10,3)

so = platform.system()

ram_total = (psutil.virtual_memory().total) / pow(10,9)
ram_used = (psutil.virtual_memory().used) / pow(10,9)
ram_percent = psutil.virtual_memory().percent

if (so == 'Windows'):
# DIRETÓRIO PARA WINDOWS
    disc_total = psutil.disk_usage('C:\\').total / pow(10,9)
    disc_used = psutil.disk_usage('C:\\').used / pow(10,9)
    disc_percent = psutil.disk_usage('C:\\').percent
elif (so == 'Linux'):
    disc_total = psutil.disk_usage('/bin').total / pow(10,9)
    disc_used = psutil.disk_usage('/bin').used / pow(10,9)

    disc_percent = psutil.disk_usage('/bin').percent


def SI1():
    tela = tk.Toplevel()
    tela.title("SI-1")
    tela.configure(background="#DCDCDA")
    tela.geometry("350x300")
    tela.resizable(False, False)

    msgDiscoRam = f"""
#                ==>   PORCENT     |      TOTAL     |      USED     |
DISC(GB)  ==>   {(disc_percent*1.2):11.1f}%     |     {disc_total*1.2:9.1f}     |    {disc_used*1.2:6.1f}      |
RAM (GB) ==>   {ram_percent:11.1f}%     |     {ram_total:11.1f}     |    {ram_used:8.1f}      |
"""

    msgCpu = f"""
#          ==>     PORCENT     |      SPEED     |   MAX SPEED    |
CPU     ==>           {cpu_porcent*1.15:6.1f}%     |   {cpu_speed*1.15:3.2f}GHz    |   {cpu_speed_max*1.15:10.2f}GHz     |
"""
    
    label_usuario = Label(tela, border=4, bg= "#C2C2C2", highlightbackground="black",highlightthickness=1, text="Usuário", anchor=W, justify=LEFT)
    label_usuario.place(relx= 0.05,rely= 0.05, relwidth=0.2, relheight= 0.1, anchor=NW)
    
    label_cpu = Label(tela, border=4, bg= "#C2C2C2", highlightbackground="black",highlightthickness=1, text=msgCpu, anchor=W, justify=LEFT)
    label_cpu.place(relx= 0.05,rely= 0.5, relwidth=0.9, relheight= 0.2, anchor=W)

    label_disco_ram = Label(tela, border=4, bg= "#C2C2C2", highlightbackground="black",highlightthickness=1, text=msgDiscoRam, anchor= NW, justify=LEFT)
    label_disco_ram.place(relx= 0.05,rely= 0.8, relwidth=0.9, relheight= 0.3, anchor=W)
    

def MI1():
    tela = tk.Toplevel()
    tela.title("MI-1")
    tela.configure(background="#DCDCDA")
    tela.geometry("350x300")
    tela.resizable(False, False)

    msgDiscoRam = f"""
#                ==>   PORCENT     |      TOTAL     |      USED     |
DISC(GB)  ==>   {disc_percent:11.1f}%     |     {disc_total:9.1f}     |    {disc_used:6.1f}      |
RAM (GB) ==>   {ram_percent:11.1f}%     |     {ram_total:11.1f}     |    {ram_used:8.1f}      |
"""

    msgCpu = f"""
#          ==>     PORCENT     |      SPEED     |   MAX SPEED    |
CPU     ==>           {cpu_porcent*0.9:6.1f}%     |   {cpu_speed*0.9:3.2f}GHz    |   {cpu_speed_max*0.9:10.2f}GHz     |
"""

    label_usuario = Label(tela, border=4, bg= "#C2C2C2", highlightbackground="black",highlightthickness=1, text="Usuário", anchor=W, justify=LEFT)
    label_usuario.place(relx= 0.05,rely= 0.05, relwidth=0.2, relheight= 0.1, anchor=NW)
    
    label_cpu = Label(tela, border=4, bg= "#C2C2C2", highlightbackground="black",highlightthickness=1, text=msgCpu, anchor=W, justify=LEFT)
    label_cpu.place(relx= 0.05,rely= 0.5, relwidth=0.9, relheight= 0.2, anchor=W)

    label_disco_ram = Label(tela, border=4, bg= "#C2C2C2", highlightbackground="black",highlightthickness=1, text=msgDiscoRam, anchor= NW, justify=LEFT)
    label_disco_ram.place(relx= 0.05,rely= 0.8, relwidth=0.9, relheight= 0.3, anchor=W)

def MI2():
    tela = tk.Toplevel()
    tela.title("MI-2")
    tela.configure(background="#DCDCDA")
    tela.geometry("350x300")
    tela.resizable(False, False)

    msgDiscoRam = f"""
#                ==>   PORCENT     |      TOTAL     |      USED     |
DISC(GB)  ==>   {disc_percent*0.95:11.1f}%     |     {disc_total*0.95:9.1f}     |    {disc_used*0.95:6.1f}      |
RAM (GB) ==>   {ram_percent*0.85:11.1f}%     |     {ram_total*0.85:11.1f}     |    {ram_used*0.85:8.1f}      |
"""

    msgCpu = f"""
#          ==>     PORCENT     |      SPEED     |   MAX SPEED    |
CPU     ==>           {cpu_porcent*0.95:6.1f}%     |   {cpu_speed*0.95:3.2f}GHz    |   {cpu_speed_max*0.95:10.2f}GHz     |
"""

    label_usuario = Label(tela, border=4, bg= "#C2C2C2", highlightbackground="black",highlightthickness=1, text="Usuário", anchor=W, justify=LEFT)
    label_usuario.place(relx= 0.05,rely= 0.05, relwidth=0.2, relheight= 0.1, anchor=NW)
    
    label_cpu = Label(tela, border=4, bg= "#C2C2C2", highlightbackground="black",highlightthickness=1, text=msgCpu, anchor=W, justify=LEFT)
    label_cpu.place(relx= 0.05,rely= 0.5, relwidth=0.9, relheight= 0.2, anchor=W)

    label_disco_ram = Label(tela, border=4, bg= "#C2C2C2", highlightbackground="black",highlightthickness=1, text=msgDiscoRam, anchor= NW, justify=LEFT)
    label_disco_ram.place(relx= 0.05,rely= 0.8, relwidth=0.9, relheight= 0.3, anchor=W)

def MI3():
    tela = tk.Toplevel()
    tela.title("MI-3")
    tela.configure(background="#DCDCDA")
    tela.geometry("350x300")
    tela.resizable(False, False)

    msgDiscoRam = f"""
#                ==>   PORCENT     |      TOTAL     |      USED     |
DISC(GB)  ==>   {disc_percent*1.05:11.1f}%     |     {disc_total*1.05:9.1f}     |    {disc_used*1.05:6.1f}      |
RAM (GB) ==>   {ram_percent*0.875:11.1f}%     |     {ram_total*0.875:11.1f}     |    {ram_used*0.875:8.1f}      |
"""

    msgCpu = f"""
#          ==>     PORCENT     |      SPEED     |   MAX SPEED    |
CPU     ==>           {cpu_porcent*1.05:6.1f}%     |   {cpu_speed*1.05:3.2f}GHz    |   {cpu_speed_max*1.05:10.2f}GHz     |
"""

    label_usuario = Label(tela, border=4, bg= "#C2C2C2", highlightbackground="black",highlightthickness=1, text="Usuário", anchor=W, justify=LEFT)
    label_usuario.place(relx= 0.05,rely= 0.05, relwidth=0.2, relheight= 0.1, anchor=NW)
    
    label_cpu = Label(tela, border=4, bg= "#C2C2C2", highlightbackground="black",highlightthickness=1, text=msgCpu, anchor=W, justify=LEFT)
    label_cpu.place(relx= 0.05,rely= 0.5, relwidth=0.9, relheight= 0.2, anchor=W)

    label_disco_ram = Label(tela, border=4, bg= "#C2C2C2", highlightbackground="black",highlightthickness=1, text=msgDiscoRam, anchor= NW, justify=LEFT)
    label_disco_ram.place(relx= 0.05,rely= 0.8, relwidth=0.9, relheight= 0.3, anchor=W)


principal()
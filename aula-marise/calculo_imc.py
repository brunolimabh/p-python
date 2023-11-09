from tkinter import *
from math import pow

class Application:
    def __init__(self, master=None):
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.quintoContainer = Frame(master)
        self.quintoContainer["pady"] = 20
        self.quintoContainer.pack()

        self.tituloAltura = Label(self.primeiroContainer, text="Quanto você mede em altura? (m) ")
        self.tituloAltura.pack()

        self.altura = Entry(self.segundoContainer)
        self.altura["width"] = 20
        self.altura.pack(side=LEFT)

        self.tituloAltura = Label(self.terceiroContainer, text="Quanto você pesa em Kg? (kg)")
        self.tituloAltura.pack()

        self.peso = Entry(self.quartoContainer)
        self.peso["width"] = 20
        self.peso.pack(side=LEFT)

        self.autenticar = Button(self.quintoContainer)
        self.autenticar["text"] = "Calcular"
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.verificaIMC
        self.autenticar.pack()

        self.mensagem1 = Label(self.quintoContainer, text="")
        self.mensagem1.pack()
        self.mensagem2 = Label(self.quintoContainer, text="")
        self.mensagem2.pack()

    #Método verificar senha
    def verificaIMC(self):
        peso = self.peso.get()
        peso = float(peso)
        altura = self.altura.get()
        altura = float(altura)
        IMC = peso/(altura**2)
        IMC = float(IMC)
        self.mensagem1["text"] = 'O seu IMC é de {:.1f}'.format(IMC)
        if IMC < 18.5:
            self.mensagem2["text"] ='Diagnóstico: Abaixo do peso normal'
        elif 18.5 <= IMC <25:
           self.mensagem2["text"] ='Diagnóstico: peso normal'
        elif 25 <= IMC <30:
            self.mensagem2["text"] ='Diagnóstico: sobrepeso'
        elif 30 <= IMC <40:
            self.mensagem2["text"] ='Diagnóstico: obeso'
        elif IMC >=40:
            self.mensagem2["text"] ='Diagnóstico: obesidade mórbida '
        

root = Tk()
Application(root)
root.mainloop()
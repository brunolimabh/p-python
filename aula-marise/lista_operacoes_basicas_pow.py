from math import floor, ceil, pow

nome = input("Insira o seu nome:")
print("Olá,", nome)
a = int(input("Informa o 1° número para a manipulação dos dados:"))
b = int(input("Informa o 2° número para a manipulação dos dados:"))
lista = [(pow(b,3)),
         (pow((-b),3)),
         (pow(a,0)),
         (pow((-a),0)),
         (pow(b,0)),
         (pow((b/5),3)),
         (pow(3,(-b))),
         (pow((a/b),(-3))),
         (pow((pow((-a),3)),4)),
         (pow(.5,3)),
         (pow(0.25,4)),
         (pow(0,4)),
         (a + (pow(0.41,b))),
         (a/4 + (pow(5,b)) - (pow(b,(-4)))),
         ((pow(b,(-3))) + pow((-4),(-5))),
         ((pow(((4/5)-(a/b)+a),(-b))) + (a/(a+(pow(3,b)) - (pow((4-5),(-b))))))
]
cont = 0
while (cont < 16):
    print("Ex", cont+1, ":", lista[cont])
    cont = cont + 1

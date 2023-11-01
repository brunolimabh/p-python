from math import floor, ceil

w = 3345.61
# arredondando
arrend = round (w,0)
print(arrend)

# arredonda para o maior ou menor num possivel
maior = int(floor(w))
menor = int(ceil(w))
print(maior, menor)


lista_processador = {"CPU", "Registrador", "Core" "CPU"}
conjunto_processador2 = set(lista_processador)

user_um = {"mysql","CPU", "RAM", "SSD1", "Google"}
user_dois = {"LoL","RAM", "CPU", "HD", "Google"}
user_tres = {"mysql","LOL", "RAM", "CPU", "Firefox"}
user_quatro = {"mysql","CPU", "RAM", "SSD1", "Google"}

inventario = user_um | user_tres
print(f"União 1 e 2: \n{inventario}\n")

inventario2 = user_um | user_dois | user_tres | user_quatro
print(f"União 1, 2, 3 e 4: \n{inventario2}\n")

inventario3 = user_um.union(user_tres)
print(f"União 1 e 2: \n{inventario3}\n")

inventario4 = user_um & user_tres
print(f"Intersecção 1 e 2: \n{inventario4}\n")

inventario5 = user_um - user_dois
print(f"Diferença 1 e 2: \n{inventario5}\n")

inventario6 = "CPU" in user_um
print(f"Pertinência: CPU in 1: {inventario6}\n")

inventario7 = "CPU" in user_um, "CPU" in user_dois, "CPU" in user_tres,"CPU" in user_quatro
print(f"CPU in todos: {inventario7}\n")




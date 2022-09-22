def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿cuantos pesos " + tipo_pesos + " tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")

menu = """
Bienvenido al conversor de monedas 💰🤑🤑💲💰🤑💲🤑

1 - pesos colombianos 
2 - pesos argentinos
3 - pesos mexicanos

Elige una opcion:"""

opcion = input(menu)

if opcion == '1':
    conversor("colombianos", 3875)
elif opcion == '2':
    conversor("argentinos", 65)
elif opcion == '3':
    conversor("mexicanos", 24)
else:
    print("Ingresa una opcion correcta por favor") 



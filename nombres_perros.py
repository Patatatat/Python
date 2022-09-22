import random

def nombres_perros():
    perros = ["Loki", "Thor", "Jack", "Spike", "Rocky", "Toby", "Scott", "Zeus", "Master Chief", "Lucky"]
    

    caracteres = perros

    nombre = []

    for i in range(1):
        caracter_random = random.choice(caracteres)
        nombre.append(caracter_random)

    nombre = "".join(nombre)
    return nombre



def run():
    nombre = nombres_perros()
    print('El nombre del perro es: ' + nombre)


if __name__ == '__main__':
    run()
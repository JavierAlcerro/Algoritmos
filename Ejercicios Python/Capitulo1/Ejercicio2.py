import random

# Representamos las cartas de espadas con números del 1 al 13
cartas_espadas = list(range(1, 14))
random.shuffle(cartas_espadas)  # Barajamos las cartas

# Función para insertar una carta en su posición correcta en la mano
def insertar_en_mano_ordenada(mano, carta):
    # Si la mano está vacía, simplemente agrega la carta
    if not mano:
        mano.append(carta)
    else:
        # Busca la posición correcta en la mano ordenada
        for i in range(len(mano)):
            if carta < mano[i]:  # Encuentra donde insertar la carta
                mano.insert(i, carta)  # Inserta la carta en la posición correcta
                return
        # Si la carta es mayor que todas las cartas en la mano, colócala al final
        mano.append(carta)

# Simulación del proceso
def ordenar_cartas(cartas):
    mano = []  # La primera mano donde vamos a ordenar las cartas
    while cartas:
        carta_visible = cartas.pop(0)  # Tomamos la carta visible (la primera de la pila)
        insertar_en_mano_ordenada(mano, carta_visible)  # Insertamos la carta en la posición correcta
        print(f"Mano actual (ordenada): {mano}")  # Mostramos la mano ordenada en cada paso
    return mano

# Ejecutamos el proceso de ordenar las cartas
print(f"Cartas desordenadas: {cartas_espadas}")
mano_ordenada = ordenar_cartas(cartas_espadas)
print(f"Cartas ordenadas: {mano_ordenada}")

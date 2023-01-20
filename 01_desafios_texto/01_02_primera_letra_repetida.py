def primera_letra_repetida(texto):

    texto_minsucula = texto.lower()
    texto_sin_espacios = texto_minsucula.replace(" ", "")
    lista_letras = []
    contadorLetras = 0
    for letra in texto_sin_espacios:
        if letra in lista_letras:
            letraRepetida = letra
            break
        else:
            lista_letras.append(letra)

    for i in texto_sin_espacios:
        # print(f'{i} {letraRepetida}')
        if i == letraRepetida:
            contadorLetras += 1

    if contadorLetras >= 2:
        print(f"La primera letra repetida encontrada es {letraRepetida} y esta {contadorLetras} veces")
    else:
        print("No se encontraron letras repetidas")
    return


print(primera_letra_repetida("saltaras"))  # a
print(primera_letra_repetida("me gusta"))   # None

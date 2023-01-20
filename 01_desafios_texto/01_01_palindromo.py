def es_palindromo(texto):
    texto_mayuscula = texto.upper()
    texto_sin_espacios = texto_mayuscula.replace(" ", "")
    print(texto_mayuscula)
    print(texto_sin_espacios)
    print(texto_sin_espacios[::-1])
    return texto_sin_espacios == texto_sin_espacios[::-1]


print(es_palindromo("Anita lava la tina"))  # True
print(es_palindromo("palindromo"))  # False

texto = "Hola Mundo"
#indice: 0123456789

print(texto)
print(texto.upper())
print(texto.lower())
print(texto.find("M"))
print(texto.find("Mun"))
#recordar explicar KeySensitive de Python

print(texto.replace("Mun", "Edmun"))

nuevoTexto = texto.replace("Mun","Edmun")
print(texto,nuevoTexto)

print("Mundo" in texto)




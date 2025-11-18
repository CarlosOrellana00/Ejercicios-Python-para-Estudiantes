lenguajes = ["Python", "Ruby", "PHP", "JavaScript", "Java"]
#insertar elmentos dentro d ela lista
lenguajes.insert(3, "Go")
#insertar un primer elemento dentro de la lista
lenguajes.insert(0, "C")
#eliminar elemento dentro de la lista
lenguajes.remove("Ruby")
#consultar elemento dentro de la lista
print("PHP" in lenguajes)
# limpiar el lsitado y que no contenga ningun solo elementos
# lenguajes.clear()

#saber el largo de nuestra lsita
print(len(lenguajes))

print(lenguajes)

#Definimos un diccionario con informacion personal
persona = {
    "nombre": "Lucía",
    "edad": 32,
    "ciudad": "Madrid"
}

#iteramos sobre las claves y valores del diccionario
for clave, valor in persona.items():
    print(f"{clave.capitalize()}: {valor}")
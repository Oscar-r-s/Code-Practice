"""
Escribir un programa que pregunte al usuario su nombre,
edad, dirección y teléfono y lo guarde en un diccionario. 
Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, 
vive en <dirección> y su número de teléfono es <teléfono>.

"""

nomUS=input("Introduce tu nombre: ")
edad=input("Introduce tu edad: ")
direccion=input("Introduce tu dirección: ")
telefono=input("Introduce tu teléfono: ")

persona={"nombre":nomUS, "edad":edad, "direccion":direccion, "telefono":telefono}

print(persona["nombre"], "tiene ", persona["edad"], " años, vive en ", persona["direccion"], " y su teléfono es ", persona["telefono"])


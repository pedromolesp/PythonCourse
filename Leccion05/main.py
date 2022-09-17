
#dict (key,value)
diccionario = {
    'IDE': 'Integrated Development Environment',
    'OOP':'Object Oriented Programming',
    'DBMS':'Database Management System'
}
print(diccionario)
#Longitud del map
print(len(diccionario))
#Acceder a un objeto (hay que usar la key)
print(diccionario['IDE'])
#Acceder a un elemento con get
print(diccionario.get('OOP'))
#Modificando un elemento
diccionario['IDE'] = 'ENTORNO DE LA CONCHA'
print(diccionario['IDE'])
#Recorrer diccionario

for termino, valor in diccionario.items():
    print(termino,valor)

for termino in diccionario.keys():
    print(termino)

for valor in diccionario.values():
    print(valor)
#Comprobar si la llave existe
print('IDE' in diccionario)
# Agregar un elemento

diccionario['PK'] = 'Primary Key'
print(diccionario)


#Eliminar un elemento

diccionario.pop('DBMS')
print(diccionario)

#Vaciar el map

diccionario.clear()
print(diccionario)
#Eliminar variable del map
del diccionario
print(diccionario)





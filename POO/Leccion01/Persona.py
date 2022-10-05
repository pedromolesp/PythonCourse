class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad


    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        print("llamando método set nombre"+nombre)
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad}')

persona1 = Persona("Pedro","Molina",27)
print(persona1.nombre)
persona1.nombre = "Brujo"
print(persona1.nombre)

# persona1.mostrar_detalle()
# persona1.telefono = '664612349'
# print(persona1.telefono)
# print(f'Objeto persona 1: {persona1.nombre} {persona1.apellido} {persona1.edad}')

# Persona.mostrar_detalle(pers ona1)

# persona2 = Persona("Fernando","Cuadros",24)
# persona2.mostrar_detalle()
# print(persona2.telefono)

# print(f'Objeto persona 2: {persona2.nombre} {persona2.apellido} {persona2.edad}')

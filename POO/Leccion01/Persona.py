class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

persona1 = Persona("Pedro","Molina",27)
print(f'Objeto persona 1: {persona1.nombre} {persona1.apellido} {persona1.edad}')

persona1.nombre = "Periquillo"
persona1.apellido = "Juarez"
print(f'Objeto persona 1: {persona1.nombre} {persona1.apellido} {persona1.edad}')

persona2 = Persona("Fernando","Cuadros",24)
print(f'Objeto persona 2: {persona2.nombre} {persona2.apellido} {persona2.edad}')

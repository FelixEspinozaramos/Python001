#este es un comentarios
from calendar import c
from importlib.util import module_for_loader


edad = 30 

nombre = 'Felix'

apellido = "Espinoza"

#No se puede usar comilla invertidas Alt + 96

#Para usar saltos de parrabo se debe usar triple comilla simple
Mensaje = '''El dia de hoy'
empezo el modulo
backend'''

#se usa doble comillas para palabras que usan comillas en su composicion.
lastName = "O'neil"

print(nombre)

#En python se usa none para asignar un valor nulo
especialidad = None

#Para saber el tipo de variable se usa Type

print(type(nombre))


# tambien se puede declara varias variables 

curso, grupo, mes, dia, nota = 'codigo','Backend', 'octubre',10 , 15.4

print(grupo)

#id(var) > mostar la posicion de memoria en la cual se esta alojando la variable, funcion, clase , etc
print(id(curso))

#para eliminar la variable se usa del = delit

del curso

print(curso)
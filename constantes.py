import math

print('*** Constantes en Python ***')

PI = 3.14159
print('El valor de PI es:', PI)

NOMBRE_BASE_DATOS = 'Clientes_db'
print('Nombre de la base de datos:', NOMBRE_BASE_DATOS)

# esto no se debe hacer, no se debe modificar el valor de una constante
NOMBRE_BASE_DATOS = 'listado_clientes_db'
print('No cambiar el valor de una constante:', NOMBRE_BASE_DATOS)

# usar una constante del lenguaje Python, aunque en este caso no está en mayúsculas
print('Valor de math.pi', math.pi)

"""2.Crear un entorno virtual y aplicar lo siguiente (4 ptos):
Reglas:
- El nombre del entorno virtual tendrá el nombre con la siguiente estructura (apellido_nombre_edad)
- Instalar las siguientes librerías: Django: 5.0.6, fastapi: 0.112.0, numpy: 2.0.0 y aws (última versión)
- Generar el archivo de requirements.txt (mostrar las librerías instaladas)
- Crear un segundo archivo en el cual se creará una lista vacía, para luego agregar los datos de nombre, salario,
edad, compañía y bono a esta lista vacía (todos estos datos ya fueron obtenidos en el problema anterior)
- Caso: Reporte de calificaciones:
Se tiene un alumno con calificaciones en tres cursos: Matemáticas: 17, Ciencia: 14, Historia: 15
Cada curso tiene un peso diferente en la nota final: Matemáticas: 40%, Ciencia: 30%, Historia: 30%
Realizar lo que se pide a continuación:

Calcula la nota final ponderada del alumno.
Muestra un mensaje como: "La nota final es: 15.6" con 1 decimal.
Evalúa si el alumno aprueba (nota final >= 13.0). Muestra un mensaje booleano:
"¿Aprobado?: True" o "¿Aprobado?: Sí"
Genera una cadena resumen que diga:
"El estudiante obtuvo una nota final de 15.6 y su estado final es: Aprobado"
En caso no apruebe indicar lo contrario en los mensajes."""

# Crear lista
lista_1 = ["Rodrigo Loyola", 2500, 37, "DIRIS", 250]

# Crear variables
cali_mate = 17
cali_cie = 14
cali_his = 15
peso_mat = 0.4
peso_cie = 0.3
peso_his = 0.3

# Cálculo del ponderado
ponderado = ((cali_mate * peso_mat) + (cali_cie * peso_cie) + (cali_his * peso_his)) / (peso_mat + peso_cie + peso_his)
print("La nota final es: {}".format(f'{ponderado:.1f}'))

# Utilizar if
if ponderado >= 13.0:
    ap = "Aprobado"
else:
    ap = "Desaprobado"

# Generar mensaje final
print("El estudiante Rodrigo Loyola obtuvo una nota final de {} y su estado final es: {}".format(ponderado, ap))

"""
Escriba un programa donde tendrá los siguientes requisitos (4 ptos):
Reglas:
- Crear una función llamada procesar_notas(estudiantes) la cual va a recibir
un diccionario donde las claves serán los nombres de los estudiantes y sus
valores serán listas con 3 notas.
- Calcular el promedio de cada estudiante.
- Devolver un nuevo diccionario donde la clave sea el nombre del estudiante
y el valor sea otro diccionario con:
    promedio: que será el promedio de notas
    estado: “aprobado” si es mayor o igual a 11, “desaprobado” si es menor
- Mostrar en pantalla el estudiante con mayor promedio
"""
diccionario_1 = {"Jair": [15, 9, 11], "Pedro": [14, 5, 12], "Camila": [17, 18, 17]}

for estudiante in diccionario_1:
    notas = diccionario_1[estudiante]
    promedio = sum(notas) / len(notas)
    print("El promedio de {} es {}".format(estudiante, f'{promedio:.1f}'))

if promedio >= 11:
    estado = "Aprobado"
else:
    estado = "Desaprobado"

diccionario_2 = {promedio: estado}
diccionario_3 = {estudiante: diccionario_2}

for estudiante in diccionario_3:
    print("El diccionario actualizado es: {}".format(diccionario_3))


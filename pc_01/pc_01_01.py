"""1. Usando los tipos de datos y sus conversiones realizar lo siguiente. (4 ptos)
Reglas:
- Asignar en variables los datos de tu nombre, salario, edad y compañía para un usuario e identificar sus tipos de variables
- Edad tiene que ser tipo string, para usarla más adelante tiene que aplicarse una conversión de datos
- Identificar si la edad es mayor a 30, mostrar un mensaje ingresado “Usted tiene un bono de 10% en el mes de diciembre” caso
contrario mostrar “Usted tiene un bono del 5% en el mes diciembre”
- Mostrar el bono final que es: potencia de 2 del salario más el 5 o 10 % de su salario, según corresponda."""

# Creación de variables
nombre = "Rodrigo Loyola"
salario = 2500
edad = "37"
compania = "DIRIS"

# Conversión de variable edad
edad_2 = int(edad)
print(edad_2)

# Identificación de tipos de variables
print("La variable nombre es de tipo {}".format(type(nombre)))
print("La variable salario es de tipo {}".format(type(salario)))
print("La variable edad es de tipo {}".format(type(edad)))
print("La variable compañía es de tipo {}".format(type(compania)))
print("La variable edad_2 es de tipo {}".format(type(edad_2)))

# Identificar si la edad es mayor a 30
if edad_2 > 30:
    print("Usted tiene un bono de 10% en el mes de diciembre")

# Calcular potencia y porcentaje del salario
salario_potencia = pow(salario, 2)
salario_porcentaje = salario * 10 / 100
print(salario_potencia + salario_porcentaje)

"""1. Crear 2 variables enteras, 2 varaibles flotanes, 2 variable string, 1 variables string con contenido
netamiente numérico y una variable boolean
2. Obtener y mostrar la suma de una variable entera con la variable string numérica
(Conversiones, realizarla si fuera necesario)
3. Obtener y mostrar la suma de las 2 variables enteras más la variable string numérica y la variable flotantes
4. Obterner y mostrar el módulo de las variables enteras: %
5. Obtener y mostrar el resultado o la parte entera de las 2 variables int: //
6. Obtener una potencia usando una de las variables foltantes como base y la variable entera como pontencia

Nota: Las variables string pueden ser tu nombre y apellido"""

# Creación de variables
peso = 60 # kg
altura = 1.68 # metros
sueldo = 2500 # soles
exp_lab = 5.3 # años
nombre = "Rodrigo"
apellido = "Loyola"
edad = "37" # años
activo = True
inactivo = False
edad_1 = int(edad) # años

# Sumatoria de int + string numérico
sum_1 = exp_lab + edad_1
print(sum_1)

# Sumatoria de 2 int + 2 string numérico + 2 flotantes
sum_2 = peso + sueldo + edad_1 + altura + exp_lab
print(sum_2)

# Cálculo del modulo de los 2 int
mod_1 = sueldo % peso
mod_2 = peso % sueldo
print(mod_1)
print(mod_2)

# División de variables int
div_1 = sueldo // peso
div_2 = peso // sueldo
print(div_1)
print(div_2)

# Calculando potencia
pot_1 = pow(exp_lab, peso)
print(f'{pot_1:.2f}')
print(pot_1)

if sueldo > 0:
    categoria = "activo"
else:
    categoria = "inactivo"

print('Hola, soy {} {}, tengo {} años, mido {} metros y peso {} kg. Actualmente trabajo y gano {} soles, por tanto estoy {} en la pea'.format(nombre, apellido, edad_1, altura, peso, sueldo, categoria))



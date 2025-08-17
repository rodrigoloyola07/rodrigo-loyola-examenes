"""
Escriba un programa donde tendrá los siguientes requisitos (4 ptos):
Reglas:
- Crear una clase llamada Empleado donde sus atributos deben ser
nombre, edad, sueldo y de nacionalidad peruana, tendrá un método para
solicitar su nombre y otro para solicitar su edad. Así como un método
cumpleaños donde cada vez que invoque aumentará en un año la edad de la
persona.
- Crear la instancia de la clase Empleado y usar el nuevo método
aumentoSueldo que incrementar su sueldo en un 30% (mínimo instanciar la
clase 2 veces, mostrar por pantalla dicho sueldo ya incrementado).
- Crear un siguiente método prediccion() que retorne un mensaje donde
indique que: “En el año XXXX tendrá XX años”, el año se ingresará por
parámetro y la edad también, realizar una validación si la edad ingresada por
parámetro es menor a la del constructor indicar que no es posible realizar la
operación (Mostrar por pantalla este valor)
Aplicando la definición de Herencias. Crear una clase llamada Persona
(Que heredará de la anterior Clase) y agregar un atributo sueldo a esta
clase
- Crear un método transferencia y mostrar saldo (mostrará el saldo actual
que tiene la persona) para la clase mencionada
- El método transferencia hace que la clase Empleado que llame al método
pueda transferir la cantidad monto al objeto Empleado2 por consiguiente
deberá ir actualizando también el saldo o monto que tiene el otro empleado
en su cuenta cada vez que use el método transferencia

- Comprobar si no se tiene dinero suficiente no se ejecuta la acción e
imprimir “Saldo insuficiente”. Comprobar instanciado la clase realizando una
transferencia y con dos personas.
"""

empleado = {"nombre": input("Ingrese su nombre: "), "edad": int(input("Ingrese su edad: ")), "sueldo": int(input("Ingrese su sueldo: ")), "nacionalidad": "peruana"}
print(empleado)

empleado["edad"] = empleado["edad"] + 1
empleado["sueldo"] = empleado["sueldo"] * 1.3
print(empleado)

empleado["sueldo"] = empleado["sueldo"] * 1.3
print(empleado)

anio_actual = int(input("Ingrese año actual: "))
anio_futuro = int(input("Ingrese año futuro: "))
diferencia = anio_futuro - anio_actual
edad_futura = empleado["edad"] + diferencia
if anio_futuro < anio_actual:
    print("El año futuro es menor al actual")
else:
    print("En el año {}, usted tendrá {} años.".format(anio_futuro, edad_futura))





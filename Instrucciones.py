mi_variable = 12
print mi_variable

# Los Comentarios se separan con 2 espacios donde haya una linea de codigo 
"""Cometario de varias lineas
asas
asas"""
a = -5  # Numero negativo
a = 10 + 5  #suma
a = 12 - 7  #Resta
a = 12.5 / 2  # Division
a = 12.5 // 2  # Division entera
a = 2 ** 3  # Pontencia
a = 27 % 4  # Modulo
a = 7 * 5  # Multiplicacion

mi_tupla = ('cadena de texto', 15, 2.8, 'otro dato', 25)
print mi_tupla[1]  # Salida: 15
print mi_tupla[1:4]  # Devuelve: (15, 2.8, 'otro dato')
print mi_tupla[3:]  # Devuelve: ('otro dato', 25)
print mi_tupla[:2]  # Devuelve: ('cadena de texto', 15)

mi_lista = ['cadena de texto', 15, 2.8, 'otro dato', 25]
print mi_lista[1]  # Salida: 15
print mi_lista[1:4]  # Devuelve: [15, 2.8, 'otro dato']
print mi_lista[-2]  # Salida: otro dato
mi_lista[2] = 3.8  # el tercer elemento ahora es 3.8
mi_lista.append('Nuevo Dato')

mi_diccionario = {'clave_1': valor_1, 'clave_2': valor_2, 'clave_7': valor_7}
print mi_diccionario['clave_2']  # Salida: valor_2
del(mi_diccionario['clave_2'])
mi_diccionario['clave_1'] = 'Nuevo Valor'

a, b, c = 'string', 15, True  #Asignacion multiple
==  #igual
!=  #Diferente
>  #Mayor
<  #Menor
>=  #Mayor Igual
<=  #Menor Igual

if compra <= 100:
    print "Pago en efectivo"
elif compra > 100 and compra < 300:
    print "Pago con tarjeta de débito"
else:
	print "Pago con tarjeta de crédito"

anio = 2001
while anio <= 2012:
	print "Informes del Año", str(anio)
	anio += 1

while True:
	nombre = raw_input("Indique su nombre: ")
	if nombre:
		break

mi_tupla = ('rosa', 'verde', 'celeste', 'amarillo')
for color in mi_tupla:
	print color  #La Variable color es una variable declarada en tiempo de ejecucion

def mi_funcion(nombre, apellido):
# algoritmo

#%% Tupla vs. Lista
tupla1 = ('R1',2,1.75,False)
tupla1.index(2)
tupla1.count(1.75)
#tupla1[2] = 4 #la tupla es inmutable
nueva_lista = list(tupla1)
print(nueva_lista)
['R1', 2, 1.75, False]
nueva_lista[3] = 2.67
print(nueva_lista)
['R1', 2, 1.75, 2.67]
tupla1
('R1', 2, 1.75, False)
#%% Diccionario

#%% Función input
dato_string = input('Ingrese un dato: ')
print('El dato ingresado es: ', dato_string)
print('El tipo del dato ingresado es: ', type(dato_string))
dato_num = int(input('Ingrese un dato: '))
print('Dato ingresado: ', dato_num,'El tipo del dato es: ', type(dato_num))
#Ejercicio Delivery
print('Buenas tardes. Le saluda el Delivery T.')
menu = {
    'Entradas': [
        'Bolón de Verde'
        'Slice de Pizza'
        'Empanada'
        ],
    'Plato fuerte' : 'Filete de pollo',
    'Bebida': 'Jugo del día'
    }
print('El menú del día es: ', menu)
print('Por favor, ingrese su orden: ') 
orden = input('Entrada: ')
print('Su orden es: ', orden + menu['Plato fuerte'] + menu['Bebida'])
#%% Sentencia de control condicional
o = []
lista = ['a','b','c','d']
texto = 'CEC EPN curso de Python Essentials'

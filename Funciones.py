def direccion(ciudad, calle, num_casa):
    print('Su ciudad es: ', ciudad)
    print('La calle de entrega es: ', calle)
    print('Su número de casa es: ', num_casa)

ci = input('Ingrese su ciudad: ')
ca = input('Ingrese su calle: ')
nc = input('Ingrese su número de casa: ')
direccion(ci, ca, nc)

def resta(num1, num2):
    print('La resta de ', num1, '-', num2, 'es: ', num1-num2)

resta(3, 2)
resta(num1 = 10, num2 = 18)

def multiplicar(numero1, numero2):
    print(numero1 * numero2)
    return (numero1 * numero2)
resultado = multiplicar(5, 2)
operacion = resultado + 1
print(operacion)
print(type(resultado))

def saludo03(lista):
    for item in lista:
        print('Hola!, ', item)
    print('')
saludo03(['Ana'])
saludo03(['Ana', 'María'])
saludo03(['Ana', 'María', 'Juana'])

def crealista(n):
    lista = []
    for item in range(1, n+1, 1):
        lista.append(item)
    return lista

print(crealista(10))

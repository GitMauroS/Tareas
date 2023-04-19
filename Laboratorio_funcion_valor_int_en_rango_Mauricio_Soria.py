def readint(prompt, min, max):
    try:
        num = int(input(prompt))
                
    except ValueError:
        print('Error: Error en el ingreso')

    else:
        if num > max:
            print('Error: El valor no está en el rango permitido ({}..{})'.format(min, max))
        elif num < min:
            print('Error: El valor no está en el rango permitido ({}..{})'.format(min, max))
        else:
            return num

v = readint("Ingrese un número del -10 al 10: ", -10, 10)

while v == None:
    v = readint("Ingrese un número del -10 al 10: ", -10, 10)
else:
    print("El número ingresado es:", v)

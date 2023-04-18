#Curso Python Essentials
#Tarea Uso de Input()
#Mauricio Soria
print('Un bendecido día estimado usuario')
print('Por favor, ingrese los siguientes datos para su registro:')
lista = []
nomb = input('Nombre: ')
lista.append(nomb)
apel = input('Apellido: ')
lista.append(apel)
ubic = input('Ubicación: ')
lista.append(ubic)
edad = input('Edad: ')
lista.append(edad)
print('Gracias. Los datos ingresados son: ')
for i in range(0,4,1):
    print(lista[i])
print('¡Bienvenido! {} {},'.format(nomb, apel),
      'su edad registrada en nuestra base de datos es de {} años,'.format(edad),
      'su nueva lavadora será entregada en {}. ¡Muchas gracias por su compra!'.format(ubic))

#Curso Python Essentials - 19/04/2023
#Tarea Mauricio Soria
#Escribir y probar una función que toma tres argumentos (un año, un mes y un día del mes)
#y devuelve los días correspondientes del año, o devuelve None si alguno de los
#argumentos es inválido.

def isYearLeap(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

def daysInMonth(year, month):
    try:
        assert year >= 0
        assert month >= 1 and month <= 12
        if isYearLeap(year):
            month_days = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
            return month_days[month]
        else:
            month_days = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
            return month_days[month]
    except (NameError, ValueError, TypeError):
        print('Ingresar únicamente números')
        return None
    except:
        print('Error, los valores ingresados deben estar en un rango de año y mes adecuados')
        return None

def dayOfYear(year, month, day):
    try:
        assert year >= 0
        assert month >= 1 and month <= 12
        assert day >= 1 and day <= 31
        if isYearLeap(year):
            month_days = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
            dias_anio = f'El año ingresado es bisiesto y tiene 366 días, \nrepartidos como se muestra a continuación (mes:días) \n{month_days}'
            return dias_anio
        else:
            month_days = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
            dias_anio = f'El año ingresado no es bisiesto y tiene 365 días, \nrepartidos como se muestra a continuación (mes:días) \n{month_days}'
            return dias_anio
    except (NameError, ValueError, TypeError):
        print('Ingresar únicamente números')
        return None
    except:
        print('Error, los valores ingresados deben estar en un rango de año, mes y día adecuados')
        return None        

print(dayOfYear(2000, 12, 31))

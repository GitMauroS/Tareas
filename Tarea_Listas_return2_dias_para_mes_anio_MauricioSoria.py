#Curso Python Essentials - 19/04/2023
#Tarea Mauricio Soria
#Escribir y probar una función que toma dos argumentos (un año y un mes) y
#devuelve el nro. de días para el par mes / año dado. Return None si sus
#argumentos no tienen sentido.

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

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]

for i in range(len(testYears)):
    yr = testYears[i]
    mo = testMonths[i]
    print(yr, mo, "->", end="")
    result = daysInMonth(yr, mo)
    if result == testResults[i]:
        print("OK")
    else:
        print("Failed")

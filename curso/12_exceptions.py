
numberOne = 5
numberTwo = "1"

try:
    print(numberOne + numberTwo)
except:
    print("ERROR")
else: # OPCIONAL
    # Se ejecuta si NO se produce una excepción
    print("Funciona correctamente")
finally: # OPCIONAL
    # Se ejecuta SIEMPRE
    print("La ejecucion continua")

try:
    print(numberOne + numberTwo)
except ValueError:
    print("ERROR TIPO VALUE ERROR")
except TypeError:
    print("ERROR TIPO TYPE ERROR")
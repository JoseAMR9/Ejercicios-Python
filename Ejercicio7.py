num1 = float(input("Digite el primer numero: "))
num2 = float(input("Digite el segundo numero: "))
signo = input("Digite el primer caracter de (suma,resta,division,multiplicacion): ").lower()

match(signo):
    case 's':
        print(f"La suma es: {num1 + num2}")
    case 'r':
        print(f"La resta es: {num1 - num2}")
    case 'm':
        print(f"La multiplicación es: {num1 * num2}")
    case 'd':
        print(f"La división es: {num1 / num2:.2f}")
    case default:
        print("Caracter incorrecto")
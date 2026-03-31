import os

saldo = 1000
while True:
    print(f"Saldo de la cuenta: ${saldo}")
    print("1.- Ingresar dinero a la cuenta")
    print("2.- Retirar dinero de la cuenta")
    print("3.- Mostrar dinero disponible")
    print("4.- Salir")
    try:
        opcion = int(input("Seleccione una opcion: "))
    except ValueError:
        print("Ingrese un número válido")
        input("\nPresione Enter para continuar...")
        os.system("cls")
        continue
    match(opcion):
        case 1:
            ingreso = float(input("\nIngrese la cantidad de dinero: "))
            if ingreso < 0:
                print("Ingrese un monto positivo")
            else:
                saldo += ingreso
                print(f"El nuevo saldo es de: ${saldo}")
        case 2:
            retirar = float(input("\nIngrese la cantidad de dinero a retirar: "))
            if retirar > saldo:
                print("No tiene esa cantidad de dinero para retirar")
            else:
                saldo -= retirar
                print(f"El nuevo saldo es de: ${saldo}")
        case 3:
            print(f"\nEl saldo restante es de: {saldo}")
        case 4:
            print("\nGracias por usar el cajero")
            break
        case _:
            print("\nElija una opcion correcta")
    input("\nPresione Enter para continuar...")
    os.system("cls")


def suma_digitos(numero):
    if numero < 10:
        return numero
    return (numero % 10) + suma_digitos(numero // 10)
num = int(input("Número: "))
print("Suma de dígitos:", suma_digitos(num))

def decimal_a_binario(num):
    if num == 0:
        return ""
    return decimal_a_binario(num // 2) + str(num % 2)
numero = int(input("Número decimal: "))
binario = decimal_a_binario(numero)
print(f"Binario: {binario if binario else '0'}")

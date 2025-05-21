def contar_digito(numero, digito):
    if numero == 0:
        return 0
    return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)
num = int(input("Número: "))
dig = int(input("Dígito a contar: "))
print(f"El dígito {dig} aparece {contar_digito(num, dig)} veces")

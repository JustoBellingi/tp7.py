def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

# Prueba
b = int(input("Base: "))
e = int(input("Exponente: "))
print(f"{b}^{e} = {potencia(b, e)}")

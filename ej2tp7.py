def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    return fibonacci(num - 1) + fibonacci(num - 2)
posicion = int(input("Ingresá una posición para la serie de Fibonacci: "))
for i in range(posicion + 1):
    print(f"f({i}) = {fibonacci(i)}")

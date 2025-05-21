def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
num = int(input("Ingrese un número: "))
for i in range(1, num + 1):
    print(f"{i}! = {factorial(i)}")


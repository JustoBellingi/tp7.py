def contarBloques(num):
    if num == 1:
        return 1
    return num + contarBloques(num - 1)
niveles = int(input("Niveles de la pirámide: "))
print("Total de bloques:", contar_bloques(niveles))

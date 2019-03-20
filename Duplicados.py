def duplicados(array):
    if len(array) == 0:
        return "array vacio"
    else:
        m = max(array) + 1
        count = [0] * m  # inicializa con ceros
        res = []
        for i in range(len(array)):
            if count[array[i]] != 1:  # si no lo he contado, lo cuento y agrego
                count[array[i]] += 1  # conteo
                res.append(array[i])  # agrega elemento al array respuesta

        return res


# PRUEBAS
# 1 -> array vacio
print(duplicados([]))
# 2 -> un solo elemento
print(duplicados([0]))
# 3 -> sin duplicados
print(duplicados([1, 2, 4, 8, 3, 5, 6]))
# 4 -> duplicados con numeros pequeños
print(duplicados([6, 1, 1, 2, 3, 2, 1, 1, 1, 2, 3]))
# 5 -> duplicados con numeros pequeños y grandes
print(duplicados([1, 20, 2, 1000000, 210, 300, 50000, 1000, 210, 20, 1000, 1000000, 1000, 50000]))


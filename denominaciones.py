
# retorna True si existe un forma de cambiar el valor con las denominaciones del array, False si no hay

def cambioDenominaciones(deno, v):
    n = len(deno)

    subset = ([[False for i in range(v + 1)] for i in range(n + 1)])

    for i in range(n + 1):
        subset[i][0] = True

        for i in range(1, v + 1):
            subset[0][i] = False

        for i in range(1, n + 1):
            for j in range(1, v + 1):
                if j < deno[i - 1]:
                    subset[i][j] = subset[i - 1][j]
                if j >= deno[i - 1]:
                    subset[i][j] = (subset[i - 1][j] or subset[i - 1][j - deno[i - 1]])

        # cache
        #for i in range(n+1):
         #   for j in range(s+1):
          #      print(subset[i][j], end=" ")
        #print()
    return subset[n][v]


# sets de prueba:
deno = [3, 4, 2]
v = 8
print(cambioDenominaciones(deno, v))

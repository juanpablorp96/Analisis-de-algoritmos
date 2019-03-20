import numpy
from random import randint
from time import time
import matplotlib.pyplot as plt


def mul_mat(n):
    # creation of matrices
    a = numpy.zeros(shape=(n, n), dtype=int)
    b = numpy.zeros(shape=(n, n), dtype=int)
    c = numpy.zeros(shape=(n, n), dtype=int)

    for i in range(n):
        for j in range(n):
            # random numbers
            a[i][j] = randint(0, 99)
            b[i][j] = randint(0, 99)

    print("Matrix A => \n", a)
    print("Matrix B => \n", b)

    # multiplication
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] += a[i][k] * b[k][j]

    print("Result => \n", c)


l_times = []
l_size = []
# tests
for x in range(10, 1001, 50):
    t_initial = time()
    mul_mat(x)
    t_final = time()
    # execution time
    t_exe = t_final - t_initial
    l_times.append(t_exe * 1000)
    l_size.append(x)
    print("Tiempo de ejecucion matriz", x, "x", x, t_exe * 1000, "milisegundos")

print(l_times)
print(l_size)
# graphic
plt.title("Multiplicacion de matrices")
plt.ylabel("Tiempo en milisegundos")
plt.xlabel("Tamaño de la matriz cuadrada")
plt.plot(l_size, l_times)
plt.show()




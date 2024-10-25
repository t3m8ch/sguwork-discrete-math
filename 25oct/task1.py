import numpy as np


def read_m():
    n = int(input("Введите размерность матрицы n: "))
    print("Введите матрицу")

    m = []
    for row in range(n):
        m.append([bool(int(x)) for x in input().split()])

    return np.array(m)


def print_m(m):
    for row in m:
        print(*[int(x) for x in row], sep="\t")


def is_reflexive(m):
    return np.all(np.diag(m))


def is_antisymmetry(m):
    return np.all(np.logical_and(m, np.transpose(m)) <= np.identity(m.shape[0]))


def is_transitive(m):
    return np.all(np.dot(m, m) <= m)


m = read_m()
print_m(m)

reflexive = is_reflexive(m)
print(f"Reflexive: {reflexive}")

antisymmetry = is_antisymmetry(m)
print(f"Antisymmetry: {antisymmetry}")

transitive = is_transitive(m)
print(f"Transitive: {transitive}")

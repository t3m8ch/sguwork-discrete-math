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
        print(*[int(x) for x in row], sep=" ")


m = read_m()

def is_reflexive(m):
    return np.all(np.diag(m))


def is_antisymmetry(m):
    return np.all(np.logical_and(m, np.transpose(m)) <= np.identity(m.shape[0]))


def is_transitive(m):
    return np.all(np.dot(m, m) <= m)

reflexive = is_reflexive(m)
print(f"Reflexive: {reflexive}")

antisymmetry = is_antisymmetry(m)
print(f"Antisymmetry: {antisymmetry}")

transitive = is_transitive(m)
print(f"Transitive: {transitive}")


print("Проверка на антисимметричность:")
print()
print("Транспонируем матрицу")
print_m(np.transpose(m))
print()
print("Логическое умножение")
print_m(np.logical_and(m, np.transpose(m)))
print()
print()

print("Проверка на транзитивность")
print()
print("Перемножаем матрицы")
print_m(np.dot(m, m))
print()
print()

el = input("Введите элементы: ").split()

b = []
for i in range(m.shape[0]):
    for j in range(m.shape[1]):
        if m[i][j]:
            b.append(f"({el[i]}, {el[j]})")


print(*b, sep=", ")

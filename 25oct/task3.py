import numpy as np

xa = [1, 2, 3, 4, 6, 12, 14, 28, 42, 420]
a = [(i, j) for i in xa for j in xa if i % j == 0]

xb = [10, 11, 13, 14, 15, 20, 25, 40, 50]
b = [(i, j) for i in xb for j in xb if i > j]

xc = [10, 11, 13, 14, 15, 20, 25, 40, 50]
c = [(i, j) for i in xc for j in xc if i < j]


def b_to_m(b, x):
    res = []
    for i in x:
        row = []
        for j in x:
            if (i, j) in b:
                row.append(True)
            else:
                row.append(False)
        res.append(row)
    return np.array(res)


def print_m(m):
    print("== МАТРИЦА ==")
    for row in m:
        print(*[int(x) for x in row], sep=" ")


def is_reflexive(m):
    return np.all(np.diag(m))


def is_antireflexive(m):
    return not np.any(np.diag(m))


def is_symmetry(m):
    print("== Проверка на симметричность: ==")
    print("= Транспонируем матрицу =")
    print_m(np.transpose(m))
    return np.array_equal(np.transpose(m), m)


def is_antisymmetry(m):
    print("== Проверка на антисимметричность: ==")
    print("= Транспонируем матрицу =")
    print_m(np.transpose(m))
    print("= Логическое умножение =")
    print_m(np.logical_and(m, np.transpose(m)))

    return np.all(np.logical_and(m, np.transpose(m)) <= np.identity(m.shape[0]))


def is_transitive(m):
    print("== Проверка на транзитивность ==")
    print("= Перемножаем матрицы =")
    print_m(np.dot(m, m))
    return np.all(np.dot(m, m) <= m)


def is_full(b, x):
    print("== Проверка на полноту: ==")
    return all(((i, j) in x or (j, i)) in x for i in x for j in x)


print("a)")
print(xa)
print(a)
ma = b_to_m(a, xa)
print_m(ma)
print()
print(is_reflexive(ma))
print()
print(is_antireflexive(ma))
print()
print(is_symmetry(ma))
print()
print(is_antisymmetry(ma))
print()
print(is_transitive(ma))
print()
print(is_full(a, xa))
print()

print("b)")
print(xb)
print(b)
print()
mb = b_to_m(b, xb)
print_m(mb)
print()
print(is_reflexive(mb))
print()
print(is_antireflexive(mb))
print()
print(is_symmetry(mb))
print()
print(is_antisymmetry(mb))
print()
print(is_transitive(mb))
print()
print(is_full(b, xb))
print()

print("c)")
print(xc)
print(c)
print()
mc = b_to_m(c, xc)
print_m(mc)
print()
print(is_reflexive(mc))
print()
print(is_antireflexive(mc))
print()
print(is_symmetry(mc))
print()
print(is_antisymmetry(mc))
print()
print(is_transitive(mc))
print()
print(is_full(c, xc))
print()

import numpy as np

# Функция для вычисления определителя матрицы
def determinant(matrix):
    return np.linalg.det(matrix)

# Функция для решения системы уравнений методом Крамера
def cramer_rule(A, B):
    n = len(A)
    if len(B) != n or len(A[0]) != n:
        raise ValueError("Некорректные размеры матрицы или вектора")

    detA = determinant(A)
    if detA == 0.0:
        raise RuntimeError("Определитель матрицы коэффициентов равен нулю, метод Крамера не применим.")

    solutions = []

    for i in range(n):
        Ai = np.array(A, copy=True)  # Копируем матрицу A
        # Заменяем i-й столбец на вектор B
        for j in range(n):
            Ai[j][i] = B[j]
        solutions.append(determinant(Ai) / detA)

    return solutions

if __name__ == "__main__":
    try:
        # Матрица коэффициентов системы уравнений
        A = [
            [1, 1, 1, 1],
            [5, -3, 2, -8],
            [3, 5, 1, 4],
            [4, 2, 3, 1]
        ]

        # Вектор правой части
        B = [0, 1, 0, 3]

        # Решение системы методом Крамера
        solutions = cramer_rule(A, B)

        # Вывод результатов
        print("Result:")
        for i, solution in enumerate(solutions):
            print(f"x{i + 1} = {solution}")
    except Exception as e:
        print(f"Error: {e}")


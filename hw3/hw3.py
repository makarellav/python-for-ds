import numpy as np

MIN = 1
MAX = 225
SIZE = 15


# 1.    Створіть двовимірний масив 15x15, що складається з чисел від 1 до 225.
def generate_2d_array() -> np.ndarray:
    return np.arange(MIN, MAX + 1).reshape(SIZE, SIZE)


# 2.    Обчисліть суму по кожному стовпцю та збережіть результати у вигляді одновимірного масиву.
def sum_columns(arr: np.ndarray) -> np.ndarray:
    return arr.sum(axis=0)


# 3.    Знайдіть стандартне відхилення елементів масиву.
def calculate_std(arr: np.ndarray) -> float:
    return arr.std()


# 4.    Виконайте транспонування масиву.
def transpose(arr: np.ndarray) -> np.ndarray:
    return arr.T


def solve_homework_3():
    arr = generate_2d_array()
    print(f"Generated array:\n{arr}")

    column_sums = sum_columns(arr)
    print(f"Column sums: {column_sums}")

    std = calculate_std(arr)
    print(f"Standard deviation: {std}")

    transposed_arr = transpose(arr)
    print(f"Transposed array:\n{transposed_arr}")

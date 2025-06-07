import numpy as np

MIN = 1
MAX = 101
COLS = 3
ROWS = 3


# Створіть двовимірний масив 3x3 з випадкових цілих чисел від 1 до 100.
def create_matrix() -> np.matrix:
    return np.matrix(np.random.randint(MIN, MAX, (ROWS, COLS)))


# Обчисліть суму всіх елементів масиву.
def sum_matrix(matrix: np.matrix) -> int:
    return np.sum(matrix)


# Знайдіть максимальне та мінімальне значення в масиві, а також їхні індекси.
def min_max_matrix(matrix: np.matrix) -> dict[str, tuple[int, int]]:
    max_value = np.matrix.max(matrix)
    min_value = np.matrix.min(matrix)
    max_index = np.unravel_index(np.argmax(matrix), matrix.shape)
    min_index = np.unravel_index(np.argmin(matrix), matrix.shape)

    return {
        "max": (max_value, max_index),
        "min": (min_value, min_index),
    }


# Відсортуйте масив по кожному рядку.
def sort_matrix(matrix):
    return np.sort(matrix, axis=1)


def solve_homework_1():
    matrix = create_matrix()
    print(f"Matrix: {matrix}\n")

    print(
        f"Sum of all elements: {sum_matrix(matrix)}\n",
    )

    min_max = min_max_matrix(matrix)
    print(
        f"Max value: {min_max['max'][0]}, Index: {min_max['max'][1]}\n",
    )
    print(
        f"Min value: {min_max['min'][0]}, Index: {min_max['min'][1]}\n",
    )

    print(f"Sorted matrix: {sort_matrix(matrix)}")

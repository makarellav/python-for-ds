import numpy as np

MIN = -100
MAX = 100
SIZE = 200

rng = np.random.default_rng()


# 1.    Створіть одновимірний масив з 200 випадкових чисел від -100 до 100.
def generate_random_array() -> np.ndarray:
    return rng.integers(MIN, MAX + 1, SIZE)


# 2.    Використовуючи маску, відфільтруйте всі додатні числа в масиві.
def filter_positive_numbers(arr: np.ndarray) -> np.ndarray:
    return arr[arr > 0]


# 3.    Замініть всі від’ємні значення на нулі.
def replace_negatives_with_zeros(arr: np.ndarray) -> np.ndarray:
    new_arr = arr.copy()

    new_arr[new_arr < 0] = 0
    return new_arr


# 4.    Обчисліть середнє значення отриманого масиву.
def calculate_mean(arr: np.ndarray) -> float:
    return arr.mean()


def solve_homework_2():
    arr = generate_random_array()
    print(f"Generated array: {arr}")

    filtered_arr = filter_positive_numbers(arr)
    print(f"Filtered array: {filtered_arr}")

    zeroed_arr = replace_negatives_with_zeros(arr)
    print(f"Zeroed array: {zeroed_arr}")

    mean = calculate_mean(zeroed_arr)
    print(f"Mean: {mean}")

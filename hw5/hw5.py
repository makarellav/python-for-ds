import pandas as pd


def solve_homework_5():
    # Створіть два DataFrame: перший містить інформацію про клієнтів (ID, ім’я, вік),
    # другий - інформацію про замовлення (ID клієнта, номер замовлення, сума).

    df_customers = pd.DataFrame(
        {
            "id": [1, 2, 3, 4, 5],
            "name": ["Олена", "Іван", "Марія", "Петро", "Софія"],
            "age": [28, 34, 22, 45, 31],
        }
    )

    print(df_customers)

    df_orders = pd.DataFrame(
        {
            "client_id": [1, 2, 1, 3, 4, 5, 2],
            "id": [101, 102, 103, 104, 105, 106, 107],
            "price": [250.0, 300.5, 150.75, 200.0, 450.0, 320.0, 275.0],
        }
    )

    print(df_orders)

    # Виконайте злиття цих DataFrame за спільним полем ID клієнта.

    df = pd.merge(
        df_customers,
        df_orders,
        how="inner",
        left_on="id",
        right_on="client_id",
    )

    # Відфільтруйте дані, залишивши лише клієнтів віком більше 30 років, які здійснили замовлення на суму більше 100.

    df_filtered = df[(df["age"] > 30) & (df["price"] > 100)]

    print(df_filtered)

    # Обчисліть загальну суму замовлень для цих клієнтів.

    df_total = df_filtered.groupby("client_id")["price"].sum()

    print(df_total)

import pandas as pd


def solve_homework_6():
    # Завантажте дані, що містять інформацію про продажі в різних містах

    df = pd.read_csv(
        "https://raw.githubusercontent.com/WuCandice/Superstore-Sales-Analysis/refs/heads/main/dataset/Superstore%20Dataset.csv"
    )

    print(df.head())

    df_cities = df.groupby("City")

    df_city_mean = df_cities["Profit"].mean()

    # Обчисліть середній дохід для кожного міста та виведіть результати у вигляді таблиці.

    print(df_city_mean)

    min_city = df_city_mean.idxmin()
    max_city = df_city_mean.idxmax()

    # Знайдіть місто з найвищим і найнижчим доходом.

    print(min_city, df_city_mean.loc[min_city])
    print(max_city, df_city_mean.loc[max_city])

    df["Order Date"] = pd.to_datetime(df["Order Date"])
    df["Month"] = df["Order Date"].dt.month

    df_month_transactions_count = df.groupby("Month").size()

    # Відобразьте кількість транзакцій для кожного місяця, використовуючи групування за датою.
    print(df_month_transactions_count)

import pandas as pd


def solve_homework_4():
    # Завантажте CSV-файл
    df = pd.read_csv("../data/titanic.csv")

    print(df)

    # Виведіть перші 5 і останні 5 рядків, щоб оглянути структуру даних.
    head_tail = pd.concat([df.head(5), df.tail(5)])

    # it prints the same result as the previous print statement :)
    print(head_tail)

    # Видаліть усі рядки з пропущеними значеннями, а також усі дублі.
    temp = df.dropna().drop_duplicates()
    print(temp)
    print(len(temp))

    # Замініть пропущені значення у стовпці з ціною на середнє значення цього стовпця.
    df["Fare"] = df["Fare"].fillna(df["Fare"].mean())

    print(df["Fare"].isna().sum())
    print(df)
    print(len(df))

from dotenv import load_dotenv
import os
import pandas as pd
import sqlalchemy as sa


def solve_howework():
    load_dotenv()

    host = os.environ.get("DB_HOST")
    user = os.environ.get("DB_USER")
    password = os.environ.get("DB_PASSWORD")
    db = os.environ.get("DB_NAME")
    port = os.environ.get("DB_PORT")

    engine = sa.create_engine(
        f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db}"
    )

    df = pd.read_sql_query(
        "select Age, Fare, Pclass, SibSp, Parch, Survived from titanic",
        engine,
    )

    df.dropna(inplace=True)

    print(df.corr().sort_values("Survived"))

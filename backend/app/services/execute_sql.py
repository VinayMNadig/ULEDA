from sqlalchemy import text
from app.database.connection import engine


def execute_sql(query: str):
    with engine.connect() as connection:
        result = connection.execute(text(query))

        rows = result.fetchall()

        columns = result.keys()

        data = []

        for row in rows:
            data.append(dict(zip(columns, row)))

        return data
from sqlalchemy import text

from app.database.connection import engine


def execute_sql(query: str):
    """
    Execute a SELECT query and return results.
    """

    try:
        with engine.connect() as connection:
            result = connection.execute(text(query))

            rows = result.fetchall()
            columns = result.keys()

            output = []

            for row in rows:
                output.append(dict(zip(columns, row)))

            return output

    except Exception as e:
        return {
            "error": str(e)
        }
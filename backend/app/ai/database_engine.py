from sqlalchemy import text

from app.database.connection_manager import connection_manager
from app.database.active_database import active_database

from app.rag.schema_reader import schema_to_text
from app.llm.sql_generator import generate_sql


class DatabaseEngine:

    @staticmethod
    def execute(question: str):

        # ------------------------------
        # Check database connection
        # ------------------------------

        if not active_database.is_connected():

            return {

                "success": False,

                "answer": "❌ No database connected.",

                "sql": "",

                "data": []

            }

        # ------------------------------
        # Read schema
        # ------------------------------

        schema = schema_to_text()

        # ------------------------------
        # Generate SQL
        # ------------------------------

        sql = generate_sql(
            schema,
            question
        )

        print("\n==========================")
        print("QUESTION :", question)
        print("SQL      :", sql)
        print("==========================\n")

        # ------------------------------
        # Execute SQL
        # ------------------------------

        session = connection_manager.get_session()

        try:

            result = session.execute(text(sql))

            rows = result.fetchall()

            columns = result.keys()

            data = [

                dict(zip(columns, row))

                for row in rows

            ]

            return {

                "success": True,

                "answer": f"I found {len(data)} record(s).",

                "sql": sql,

                "data": data,

                "rows": len(data)

            }

        except Exception as e:

            return {

                "success": False,

                "answer": str(e),

                "sql": sql,

                "data": []

            }

        finally:

            session.close()
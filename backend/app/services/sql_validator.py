from sqlalchemy import inspect
from app.database.connection_manager import connection_manager


class SQLValidator:

    @staticmethod
    def validate(sql: str):

        if connection_manager.engine is None:
            return {
                "success": False,
                "answer": "No database connected."
            }

        inspector = inspect(connection_manager.engine)

        tables = inspector.get_table_names()

        sql_upper = sql.upper()

        # Basic validation
        if "SELECT" in sql_upper:
            return {
                "success": True,
                "answer": "Valid SQL"
            }

        if any(word in sql_upper for word in [
            "INSERT",
            "UPDATE",
            "DELETE",
            "DROP",
            "ALTER",
            "CREATE"
        ]):
            return {
                "success": True,
                "answer": "Dangerous Query"
            }

        return {
            "success": False,
            "answer": "Unsupported SQL statement."
        }


sql_validator = SQLValidator()
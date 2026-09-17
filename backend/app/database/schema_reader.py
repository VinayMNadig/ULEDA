from sqlalchemy import inspect

from app.database.connection_manager import connection_manager


class SchemaReader:

    @staticmethod
    def read_schema():

        # -------------------------------
        # Check Connection
        # -------------------------------

        if connection_manager.engine is None:

            raise Exception(
                "No database connected."
            )

        inspector = inspect(
            connection_manager.engine
        )

        schema = {

            "database_type":
                connection_manager.database_type,

            "tables": []

        }

        # -------------------------------
        # Read Tables
        # -------------------------------

        for table in inspector.get_table_names():

            table_info = {

                "table_name": table,

                "columns": [],

                "primary_keys": [],

                "foreign_keys": [],

                "indexes": []

            }

            # ---------------------------
            # Columns
            # ---------------------------

            for column in inspector.get_columns(table):

                table_info["columns"].append({

                    "name":
                        column["name"],

                    "type":
                        str(column["type"]),

                    "nullable":
                        column["nullable"],

                    "default":
                        str(column.get("default"))

                })

            # ---------------------------
            # Primary Keys
            # ---------------------------

            pk = inspector.get_pk_constraint(
                table
            )

            table_info["primary_keys"] = pk.get(

                "constrained_columns",

                []

            )

            # ---------------------------
            # Foreign Keys
            # ---------------------------

            for fk in inspector.get_foreign_keys(
                table
            ):

                table_info["foreign_keys"].append({

                    "column":
                        fk["constrained_columns"],

                    "reference_table":
                        fk["referred_table"],

                    "reference_column":
                        fk["referred_columns"]

                })

            # ---------------------------
            # Indexes
            # ---------------------------

            for index in inspector.get_indexes(
                table
            ):

                table_info["indexes"].append({

                    "name":
                        index["name"],

                    "columns":
                        index["column_names"]

                })

            schema["tables"].append(
                table_info
            )

        return schema

    # =====================================
    # Convert Schema to Prompt
    # =====================================

    @staticmethod
    def schema_to_text():

        schema = SchemaReader.read_schema()

        text = ""

        text += f"Database Type : {schema['database_type']}\n\n"

        for table in schema["tables"]:

            text += f"Table : {table['table_name']}\n"

            text += "Columns:\n"

            for column in table["columns"]:

                text += (
                    f"- {column['name']} "
                    f"({column['type']})\n"
                )

            if table["primary_keys"]:

                text += (
                    "Primary Keys : "
                    + ", ".join(
                        table["primary_keys"]
                    )
                    + "\n"
                )

            if table["foreign_keys"]:

                text += "Foreign Keys:\n"

                for fk in table["foreign_keys"]:

                    text += (
                        f"- {fk['column']} -> "
                        f"{fk['reference_table']} "
                        f"{fk['reference_column']}\n"
                    )

            text += "\n"

        return text
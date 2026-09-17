from sqlalchemy import inspect

from app.database.connection_manager import connection_manager


# =====================================================
# Read Schema as Dictionary
# =====================================================

def read_schema():

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

    tables = inspector.get_table_names()

    for table in tables:

        table_info = {

            "table_name": table,

            "columns": [],

            "primary_keys": [],

            "foreign_keys": [],

            "indexes": []

        }

        # --------------------------
        # Columns
        # --------------------------

        columns = inspector.get_columns(
            table
        )

        for column in columns:

            table_info["columns"].append({

                "name":
                    column["name"],

                "type":
                    str(column["type"]),

                "nullable":
                    column["nullable"]

            })

        # --------------------------
        # Primary Keys
        # --------------------------

        pk = inspector.get_pk_constraint(
            table
        )

        table_info["primary_keys"] = pk.get(

            "constrained_columns",

            []

        )

        # --------------------------
        # Foreign Keys
        # --------------------------

        foreign_keys = inspector.get_foreign_keys(
            table
        )

        for fk in foreign_keys:

            table_info["foreign_keys"].append({

                "column":
                    fk["constrained_columns"],

                "reference_table":
                    fk["referred_table"],

                "reference_column":
                    fk["referred_columns"]

            })

        # --------------------------
        # Indexes
        # --------------------------

        indexes = inspector.get_indexes(
            table
        )

        for index in indexes:

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


# =====================================================
# Convert Schema to Text
# =====================================================

def schema_to_text():

    schema = read_schema()

    text = ""

    text += f"Database Type: {schema['database_type']}\n\n"

    for table in schema["tables"]:

        text += f"Table: {table['table_name']}\n"

        text += "Columns:\n"

        for column in table["columns"]:

            nullable = "NULL"

            if not column["nullable"]:

                nullable = "NOT NULL"

            text += (

                f"  - "

                f"{column['name']} "

                f"({column['type']}) "

                f"{nullable}\n"

            )

        if table["primary_keys"]:

            text += (

                "Primary Keys: "

                + ", ".join(

                    table["primary_keys"]

                )

                + "\n"

            )

        if table["foreign_keys"]:

            text += "Foreign Keys:\n"

            for fk in table["foreign_keys"]:

                text += (

                    f"  - "

                    f"{fk['column']} -> "

                    f"{fk['reference_table']}"

                    f"({fk['reference_column']})\n"

                )

        if table["indexes"]:

            text += "Indexes:\n"

            for index in table["indexes"]:

                text += (

                    f"  - "

                    f"{index['name']} "

                    f"{index['columns']}\n"

                )

        text += "\n"

    return text
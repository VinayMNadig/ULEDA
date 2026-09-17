import sqlite3
from pathlib import Path


# ============================================
# Database Detector
# ============================================

class DatabaseDetector:

    @staticmethod
    def detect(file_path: str):

        extension = Path(file_path).suffix.lower()

        if extension in [".db", ".sqlite", ".sqlite3"]:

            return DatabaseDetector.detect_sqlite(file_path)

        elif extension == ".sql":

            return DatabaseDetector.detect_sql_dump(file_path)

        else:

            return {

                "database_type": "Unknown",

                "supported": False,

            }


# ============================================
# SQLite Detector
# ============================================

    @staticmethod
    def detect_sqlite(file_path: str):

        conn = sqlite3.connect(file_path)

        cursor = conn.cursor()

        cursor.execute("""

        SELECT name
        FROM sqlite_master
        WHERE type='table'
        AND name NOT LIKE 'sqlite_%'

        """)

        tables = [row[0] for row in cursor.fetchall()]

        total_rows = 0

        schema = {}

        for table in tables:

            cursor.execute(

                f"PRAGMA table_info({table})"

            )

            columns = cursor.fetchall()

            schema[table] = [

                {

                    "name": column[1],

                    "type": column[2],

                    "primary_key": bool(column[5])

                }

                for column in columns

            ]

            cursor.execute(

                f"SELECT COUNT(*) FROM {table}"

            )

            total_rows += cursor.fetchone()[0]

        conn.close()

        return {

            "supported": True,

            "database_type": "SQLite",

            "tables": len(tables),

            "rows": total_rows,

            "table_names": tables,

            "schema": schema,

        }


# ============================================
# SQL Dump Detector
# ============================================

    @staticmethod
    def detect_sql_dump(file_path: str):

        return {

            "supported": True,

            "database_type": "SQL Dump",

            "tables": 0,

            "rows": 0,

            "table_names": [],

            "schema": {}

        }
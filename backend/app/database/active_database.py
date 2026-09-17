from pathlib import Path
from datetime import datetime


class ActiveDatabase:

    def __init__(self):

        self.database_path = None
        self.database_name = None
        self.database_type = None
        self.connected = False
        self.connected_at = None

    # ==========================================
    # Set Active Database
    # ==========================================

    def set_database(
        self,
        path: str,
        database_type: str,
    ):

        self.database_path = path

        self.database_name = Path(path).name

        self.database_type = database_type

        self.connected = True

        self.connected_at = datetime.now()

        print("\n========== ACTIVE DATABASE ==========")
        print("Database :", self.database_name)
        print("Path     :", self.database_path)
        print("Type     :", self.database_type)
        print("Connected:", self.connected)
        print("=====================================\n")

    # ==========================================
    # Check Connection
    # ==========================================

    def is_connected(self):

        return self.connected

    # ==========================================
    # Get Database Path
    # ==========================================

    def get_path(self):

        return self.database_path

    # ==========================================
    # Get Database Name
    # ==========================================

    def get_name(self):

        return self.database_name

    # ==========================================
    # Get Database Type
    # ==========================================

    def get_type(self):

        return self.database_type

    # ==========================================
    # Get Full Database Info
    # ==========================================

    def get_database(self):

        return {

            "connected": self.connected,

            "database_name": self.database_name,

            "database_path": self.database_path,

            "database_type": self.database_type,

            "connected_at": self.connected_at,

        }

    # ==========================================
    # Summary
    # ==========================================

    def summary(self):

        if not self.connected:

            return {

                "connected": False,

                "message": "No database connected."

            }

        return {

            "connected": True,

            "database_name": self.database_name,

            "database_path": self.database_path,

            "database_type": self.database_type,

            "connected_at": self.connected_at.strftime(
                "%Y-%m-%d %H:%M:%S"
            )

        }

    # ==========================================
    # Clear Active Database
    # ==========================================

    def clear(self):

        print("\n========== DATABASE DISCONNECTED ==========")
        print("Database :", self.database_name)
        print("===========================================\n")

        self.database_path = None
        self.database_name = None
        self.database_type = None
        self.connected = False
        self.connected_at = None


# ==========================================
# Global Instance
# ==========================================

active_database = ActiveDatabase()
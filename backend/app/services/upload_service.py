import shutil
from pathlib import Path

from fastapi import UploadFile, HTTPException

from app.database.connection_manager import connection_manager
from app.database.active_database import active_database
from app.utils.database_detector import DatabaseDetector


# ==========================================
# Upload Folder
# ==========================================

UPLOAD_FOLDER = Path("uploaded_databases")

UPLOAD_FOLDER.mkdir(
    parents=True,
    exist_ok=True
)

ALLOWED_EXTENSIONS = {
    ".db",
    ".sqlite",
    ".sqlite3",
    ".sql",
}


class UploadService:

    # ==========================================
    # Validate Extension
    # ==========================================

    @staticmethod
    def validate(filename):

        extension = Path(filename).suffix.lower()

        if extension not in ALLOWED_EXTENSIONS:

            raise HTTPException(
                status_code=400,
                detail="Unsupported database file."
            )

        return extension

    # ==========================================
    # Save File
    # ==========================================

    @staticmethod
    def save(file: UploadFile):

        destination = UPLOAD_FOLDER / file.filename

        with open(destination, "wb") as buffer:

            shutil.copyfileobj(
                file.file,
                buffer
            )

        return destination

    # ==========================================
    # Upload Database
    # ==========================================

    @staticmethod
    def upload(file: UploadFile):

        UploadService.validate(
            file.filename
        )

        path = UploadService.save(
            file
        )

        print("=" * 60)
        print("DATABASE UPLOADED")
        print("Path :", path)

        info = DatabaseDetector.detect(
            str(path)
        )

        print("Database Info :", info)

        db_type = info.get(
            "database_type"
        )

        # -----------------------------
        # SQLite
        # -----------------------------

        if db_type == "SQLite":

            print("Connecting SQLite...")

            connection_manager.connect_sqlite(
                str(path)
            )

        # -----------------------------
        # MySQL
        # -----------------------------

        elif db_type == "MySQL":

            raise HTTPException(
                status_code=400,
                detail="Use Connect Database API for MySQL."
            )

        # -----------------------------
        # PostgreSQL
        # -----------------------------

        elif db_type == "PostgreSQL":

            raise HTTPException(
                status_code=400,
                detail="Use Connect Database API for PostgreSQL."
            )

        else:

            raise HTTPException(
                status_code=400,
                detail=f"Unsupported database type : {db_type}"
            )

        print(connection_manager.status())

        active_database.set_database(
            str(path),
            db_type
        )

        return {

            "success": True,

            "message": "Database uploaded successfully.",

            "database": active_database.summary(),

            "details": info,

        }

    # ==========================================
    # List Uploaded Databases
    # ==========================================

    @staticmethod
    def list_databases():

        databases = []

        for file in UPLOAD_FOLDER.iterdir():

            if file.is_file():

                databases.append({

                    "filename": file.name,

                    "size": file.stat().st_size,

                })

        return databases

    # ==========================================
    # Delete Database
    # ==========================================

    @staticmethod
    def delete(filename):

        file = UPLOAD_FOLDER / filename

        if not file.exists():

            raise HTTPException(
                status_code=404,
                detail="Database not found."
            )

        file.unlink()

        return {

            "success": True,

            "message": "Database deleted."

        }


upload_service = UploadService()
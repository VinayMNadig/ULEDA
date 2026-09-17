from pathlib import Path
import shutil

from fastapi import APIRouter, UploadFile, File, HTTPException

from app.database.connection_manager import connection_manager
from app.database.active_database import active_database

router = APIRouter(
    prefix="/database",
    tags=["Database Manager"],
)

# =====================================================
# Upload Folder
# =====================================================

BASE_DIR = Path(__file__).resolve().parents[3]

UPLOAD_FOLDER = BASE_DIR / "uploaded_databases"

UPLOAD_FOLDER.mkdir(exist_ok=True)

# =====================================================
# Upload Database
# =====================================================

@router.post("/upload")
async def upload_database(file: UploadFile = File(...)):

    if not file.filename.endswith(".db"):

        raise HTTPException(
            status_code=400,
            detail="Only SQLite (.db) files are allowed."
        )

    save_path = UPLOAD_FOLDER / file.filename

    with open(save_path, "wb") as buffer:

        shutil.copyfileobj(file.file, buffer)

    connection_manager.connect_sqlite(str(save_path))

    return {

        "success": True,

        "message": "Database uploaded successfully.",

        "database": file.filename,

        "active_database": active_database.summary()

    }

# =====================================================
# List Uploaded Databases
# =====================================================

@router.get("/list")
def list_databases():

    databases = []

    active_name = active_database.database_name

    for db in sorted(UPLOAD_FOLDER.glob("*.db")):

        databases.append({

            "name": db.name,

            "path": str(db),

            "size": round(db.stat().st_size / 1024, 2),

            "active": db.name == active_name

        })

    return {

        "success": True,

        "count": len(databases),

        "databases": databases

    }

# =====================================================
# Connect Existing Database
# =====================================================

@router.post("/connect/{database_name}")
def connect_database(database_name: str):

    db_path = UPLOAD_FOLDER / database_name

    if not db_path.exists():

        raise HTTPException(

            status_code=404,

            detail="Database not found."

        )

    connection_manager.connect_sqlite(str(db_path))

    return {

        "success": True,

        "message": f"{database_name} connected successfully.",

        "active_database": active_database.summary()

    }

# =====================================================
# Active Database
# =====================================================

@router.get("/active")
def get_active_database():

    return active_database.summary()

# =====================================================
# Disconnect Database
# =====================================================

@router.post("/disconnect")
def disconnect_database():

    connection_manager.disconnect()

    return {

        "success": True,

        "message": "Database disconnected successfully."

    }

# =====================================================
# Delete Database
# =====================================================

@router.delete("/delete/{database_name}")
def delete_database(database_name: str):

    db_path = UPLOAD_FOLDER / database_name

    if not db_path.exists():

        raise HTTPException(

            status_code=404,

            detail="Database not found."

        )

    if active_database.database_name == database_name:

        connection_manager.disconnect()

    db_path.unlink()

    return {

        "success": True,

        "message": f"{database_name} deleted successfully."

    }

# =====================================================
# Database Status
# =====================================================

@router.get("/status")
def database_status():

    return connection_manager.status()
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.database.connection_manager import connection_manager

router = APIRouter(
    prefix="/connection",
    tags=["Database Connection"],
)


# ==========================================
# Request Model
# ==========================================

class DatabaseConnection(BaseModel):

    database_type: str

    host: str | None = None

    port: int | None = None

    username: str | None = None

    password: str | None = None

    database: str | None = None

    service_name: str | None = None

    db_path: str | None = None


# ==========================================
# Connect Database
# ==========================================

@router.post("/connect")
def connect_database(request: DatabaseConnection):

    try:

        db = request.database_type.lower()

        if db == "sqlite":

            connection_manager.connect_sqlite(
                request.db_path
            )

        elif db == "mysql":

            connection_manager.connect_mysql(
                request.host,
                request.port,
                request.username,
                request.password,
                request.database,
            )

        elif db == "postgresql":

            connection_manager.connect_postgresql(
                request.host,
                request.port,
                request.username,
                request.password,
                request.database,
            )

        elif db == "sqlserver":

            connection_manager.connect_sqlserver(
                request.host,
                request.port,
                request.username,
                request.password,
                request.database,
            )

        elif db == "oracle":

            connection_manager.connect_oracle(
                request.host,
                request.port,
                request.username,
                request.password,
                request.service_name,
            )

        else:

            raise HTTPException(
                status_code=400,
                detail="Unsupported database."
            )

        return {

            "success": True,

            "database_type": connection_manager.get_database_type(),

            "message": "Connected Successfully"

        }

    except Exception as e:

        raise HTTPException(

            status_code=500,

            detail=str(e)

        )


# ==========================================
# Disconnect
# ==========================================

@router.post("/disconnect")
def disconnect_database():

    connection_manager.close()

    return {

        "success": True,

        "message": "Database Disconnected"

    }


# ==========================================
# Current Connection
# ==========================================

@router.get("/status")
def database_status():

    return {

        "connected": connection_manager.get_database_type() is not None,

        "database_type": connection_manager.get_database_type()

    }
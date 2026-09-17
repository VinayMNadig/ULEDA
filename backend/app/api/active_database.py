from fastapi import APIRouter

from app.database.active_database import active_database

router = APIRouter(

    prefix="/active-database",

    tags=["Active Database"]

)


@router.get("/")
def current_database():

    return active_database.get_database()


@router.delete("/")
def clear_database():

    active_database.clear()

    return {

        "success": True,

        "message": "Active database cleared."

    }
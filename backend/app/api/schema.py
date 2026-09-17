from fastapi import APIRouter

from app.database.schema_reader import SchemaReader

router = APIRouter(

    prefix="/schema",

    tags=["Schema"]

)


@router.get("/")
def read_schema():

    return SchemaReader.read_schema()
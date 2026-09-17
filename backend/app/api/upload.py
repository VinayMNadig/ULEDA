from fastapi import APIRouter, UploadFile, File

from app.services.upload_service import upload_service

router = APIRouter(
    prefix="/upload",
    tags=["Database Upload"]
)


# ==========================================
# Upload Database
# ==========================================

@router.post("/")
async def upload_database(
    file: UploadFile = File(...)
):

    return upload_service.upload(file)


# ==========================================
# List Uploaded Databases
# ==========================================

@router.get("/list")
def list_databases():

    return upload_service.list_databases()


# ==========================================
# Delete Uploaded Database
# ==========================================

@router.delete("/{filename}")
def delete_database(
    filename: str
):

    return upload_service.delete(filename)
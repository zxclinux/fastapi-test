from fastapi import UploadFile, File, HTTPException
from core import db_helper
from utils.static_upload import upload_file

async def upload_image(file: UploadFile = File(...)):
    try:
        result = upload_file(file)
        db_helper.save_metadata(result)
        return {"message": "Uploaded", "data": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

async def retrieve_image(image_id: str):
    try:
        metadata = db_helper.get_metadata(image_id)
        if not metadata:
            raise HTTPException(status_code=404, detail="Image not found")
        return {"data": metadata}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
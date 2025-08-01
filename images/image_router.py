from fastapi import APIRouter, UploadFile, File, Request, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from images.image_crud import upload_image, retrieve_image

router = APIRouter(
    prefix="/images",
    tags=["Images"]
)

templates = Jinja2Templates(directory="templates")

@router.get("/upload")
async def upload_form(request: Request):
    return templates.TemplateResponse("upload.html", {"request": request})

@router.post("/upload")
async def post_image(request: Request, file: UploadFile = File(...)):
    result = await upload_image(file)
    image_id = result["data"]["imageid"]
    return RedirectResponse(url=f"/images/{image_id}", status_code=303)

@router.get("/{image_id}")
async def get_image(request: Request, image_id: str):
    response = await retrieve_image(image_id)
    if "data" not in response:
        raise HTTPException(status_code=404, detail="Image not found")
    return templates.TemplateResponse("image.html", {"request": request, "image": response["data"]})
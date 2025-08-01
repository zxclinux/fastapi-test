import uvicorn
from fastapi import FastAPI
from images.image_router import router as image_router
app = FastAPI()
app.include_router(image_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True,)
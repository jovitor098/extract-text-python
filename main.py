from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from extractText import extract_text
from fastapi.middleware.cors import CORSMiddleware
from os import environ
from exception.missingImage import MissingImageException
from exception.loadImage import LoadImageException

app = FastAPI()

origins = [
    environ.get("FRONT_URL")
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(MissingImageException)
async def missing_image_exception_handler(request: Request, exc: MissingImageException):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST, 
        content={"error": f"Check if you upload image: {exc.msg}"})

@app.exception_handler(LoadImageException)
async def missing_image_exception_handler(request: Request, exc: LoadImageException):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST, 
        content={"error": f"Check if the file is a image: {exc.msg}"})


@app.post("/extract")
async def extract(request: Request):
    form = await request.form()

    if not form.get("upload_image"):
        raise MissingImageException("Missing a image file")

    file = form.get("upload_image")
    text = await extract_text(file)
    return {"text": text}

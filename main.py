from fastapi import FastAPI, Request
from extractText import extract_text

app = FastAPI()

@app.post("/extract")
async def extract(request: Request):
    form = await request.form()
    file = form.get("upload_image")
    text = await extract_text(file)
    return {"text": text}

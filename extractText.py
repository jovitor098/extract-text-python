from PIL import Image
from io import BytesIO
import pytesseract

async def extract_text(file):
    content = await file.read()
    img = Image.open(BytesIO(content))
    text = pytesseract.image_to_string(img)
    return text

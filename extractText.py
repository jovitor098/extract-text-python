from PIL import Image
from io import BytesIO
import pytesseract
from exception.loadImage import LoadImageException

async def extract_text(file):
    try:
        content = await file.read()
        img = Image.open(BytesIO(content))
        text = pytesseract.image_to_string(img)
        return text
    except:
        raise LoadImageException("Erro while load image")

FROM python:3.13.1-slim
RUN apt-get update && apt-get install -y --no-install-recommends\
  tesseract-ocr=5.3.0-2 \
  libtesseract-dev=5.3.0-2 \
  && apt-get clean

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["fastapi", "run", "main.py"]

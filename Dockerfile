FROM python:3.12.3-slim


RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1 \
    libglib2.0-0 \
    curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


RUN mkdir -p app/models && \
    curl -L -o app/models/w600k_r50.onnx https://huggingface.co/maze/faceX/resolve/main/w600k_r50.onnx


COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

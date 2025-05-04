FROM python:3.8-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
    build-essential \
    libatlas-base-dev \
    libhdf5-dev \
    libprotobuf-dev \
    protobuf-compiler \
    python3-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . .

RUN pip install --upgrade pip setuptools wheel && \
    pip install --no-cache-dir --retries 5 --timeout 30 \
    --trusted-host pypi.org --trusted-host files.pythonhosted.org \
    -e .

# Optional: if training is lightweight and needed in the image
RUN python pipeline/training_pipeline.py

EXPOSE 5000

CMD ["python", "application.py"]
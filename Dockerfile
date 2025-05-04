FROM python:3.8-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libatlas-base-dev \
    libhdf5-dev \
    libprotobuf-dev \
    protobuf-compiler \
    python3-dev \
    curl \
    ca-certificates \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip to latest
RUN pip install --upgrade pip

WORKDIR /app
COPY . .

# Add retry + increased timeout to pip install to avoid flaky SSL
RUN pip install --default-timeout=100 --retries=5 --no-cache-dir -e .

RUN python pipeline/training_pipeline.py

EXPOSE 5000
CMD ["python", "application.py"]

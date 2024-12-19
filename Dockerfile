FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    python3-rpi.gpio \
    python3-gpiozero \
    gcc \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY dev/main.py ./

CMD ["python", "./main.py"]

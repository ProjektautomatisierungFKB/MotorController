FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY dev/pin_voltage_controller.py ./
COPY extDev/shared_utils/utils/logger.py ./

CMD ["python", "./pin_voltage_controller.py"]

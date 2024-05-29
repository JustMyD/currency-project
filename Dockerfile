FROM python:3.11-alpine

WORKDIR /app

ENV PYTHONUNBUFFERED 1

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src/ .

CMD ["uvicorn", "main:app", "--reload", "--port", "8000", "--host", "0.0.0.0"]

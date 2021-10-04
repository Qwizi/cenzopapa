FROM tiangolo/uvicorn-gunicorn:python3.9-slim

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
FROM python:3.11-slim as builder

RUN pip install --upgrade pip

WORKDIR app
COPY requirements.txt .

RUN pip install --no-cache-dir --user -r requirements.txt

COPY . .
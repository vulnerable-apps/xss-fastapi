# syntax=docker/dockerfile:1
FROM python:3.10-alpine

ENV APP_HOME=/app \
    PYTHONBUFFERED=1 \
    ENV=DOCKER

WORKDIR ${APP_HOME}

COPY requirements.txt .

RUN set -eux \
    && apk update \
    && apk add --no-cache --virtual .build-deps \
        gcc \
        libc-dev \
        linux-headers \
        python3-dev \
    && pip install --no-cache-dir -r requirements.txt

COPY . .

# fastapi
CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]


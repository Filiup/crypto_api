FROM python:3.13.2-alpine

WORKDIR /crypto

ENV PATH="/home/python/.local/bin:$PATH"

RUN apk add --no-cache \
    gcc \
    musl-dev \
    postgresql-dev \
    libpq \
    libffi-dev \
    build-base

RUN adduser -u 1000 -D python
USER python

COPY . .
RUN pip install -r requirements.txt
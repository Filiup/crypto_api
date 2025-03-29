FROM python:3.13.2-alpine

WORKDIR /crypto

RUN adduser -u 1000 -D python
USER python

COPY . .
RUN pip install -r requirements.txt
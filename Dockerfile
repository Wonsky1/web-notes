FROM python:3.11-slim-buster
LABEL maintaner="vladyslav.pidborskyi@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

RUN apt-get update \
    && apt-get -y install libpq-dev gcc

COPY . .

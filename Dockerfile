FROM python:3.8.16-buster

WORKDIR /backend

COPY ../.. .
RUN pip install -r requirements.txt
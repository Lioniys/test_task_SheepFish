FROM python:3.10-slim-buster

RUN mkdir /app

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip3 install --upgrade pip

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

RUN chmod a+x ./*.sh
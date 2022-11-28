FROM python:3.11-alpine

RUN apk add --no-cache --virtual .build-deps gcc postgresql-dev musl-dev python3-dev
RUN apk add libpq

COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt

RUN apk del --no-cache .build-deps

RUN mkdir -p /code
COPY . /code/
WORKDIR /code
EXPOSE 8080

ENTRYPOINT [ "gunicorn", "--bind=0.0.0.0:8080", "main:app" ]
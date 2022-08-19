FROM python:3.8-alpine

ENV PYTHONUNBUFFERED=1

RUN mkdir -p /app

WORKDIR /app

COPY . .

RUN apk update \
    # Pillow dependencies
    && apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev \
    # psycopg2 dependencies
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    # https://docs.djangoproject.com/en/dev/ref/django-admin/#dbshell
    && apk add postgresql-client \
    && pip install --upgrade pip

RUN pip install -r /app/requirements.txt

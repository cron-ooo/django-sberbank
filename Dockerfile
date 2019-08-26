FROM python:3.7

ENV PYTHONUNBUFFERED=1

RUN pip install -U pip setuptools wheel \
    celery==4.3.0 \
    django-braces==1.13.0 \
    django==2.2.4 \
    djangorestframework==3.10.2 \
    jsonfield==2.0.2 \
    requests==2.22.0

WORKDIR /sberbank

COPY . .

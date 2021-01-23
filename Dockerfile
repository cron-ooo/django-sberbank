FROM python:3.9

ENV PIP_NO_CACHE_DIR=off \
  PYTHONUNBUFFERED=1

RUN pip install -U pip setuptools wheel \
    django==2.2.17 \
    djangorestframework==3.10.3 \
    jsonfield==3.1.0 \
    requests==2.25.1

WORKDIR /sberbank

COPY . .

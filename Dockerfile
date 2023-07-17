FROM python:3.11-alpine3.16

EXPOSE 8000
COPY app /app/
COPY poetry.lock pyproject.toml /app/

WORKDIR /app

RUN apk add postgresql-client build-base postgresql-dev

RUN pip install --upgrade pip \
    && pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi \
    && adduser --disabled-password app-user

USER app-user

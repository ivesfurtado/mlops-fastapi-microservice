# Dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY ./src /app/src
COPY pyproject.toml poetry.lock /app/

RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev

EXPOSE 8000

CMD ["uvicorn", "src.core.server:app", "--host=0.0.0.0", "--port=80"]

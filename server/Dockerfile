FROM python:3.8-alpine
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add --no-cache postgresql-dev gcc python3-dev musl-dev bash tzdata; \
    cp /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime; \
    echo "America/Sao_Paulo" > /etc/timezone

RUN mkdir /code

WORKDIR /code

COPY . /code

RUN pip install pipenv; \
    pipenv lock --requirements > requirements.txt; \
    pipenv lock --requirements --dev-only > requirements-dev.txt

RUN pip install --no-cache-dir -r requirements.txt -r requirements-dev.txt

RUN chmod +x /code/scripts/start.sh
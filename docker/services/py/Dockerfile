FROM python:3.6-alpine

LABEL maintainer="scottrmercer" \
      description="bare bones python 3.6 with sqlalchemy"

WORKDIR /app

COPY requirements.txt ./

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip
RUN pip --no-cache-dir install -r requirements.txt

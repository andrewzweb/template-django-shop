# pull official base image
FROM python:3.8.3-alpine

# set work directory
RUN mkdir -p /srv/app
WORKDIR /srv/app

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip3 install --upgrade pip
COPY ./deploy/pip-prd.txt ./pip-prd.txt
RUN pip3 install -r pip-prd.txt

# copy project
COPY . .

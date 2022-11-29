FROM python:latest as builder-base

RUN apt-get update -y && apt-get upgrade -y

FROM builder-base as builder

ADD . /workspace
WORKDIR /workspace

COPY app .
RUN poetry install && poetry build
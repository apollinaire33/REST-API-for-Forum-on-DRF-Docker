FROM python:3.8.5

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHOUNBUFFERED 1

WORKDIR /usr/src/

COPY ./requiements.txt /usr/src/requiements.txt
RUN pip install -r /usr/src/requiements.txt

COPY . /usr/src/
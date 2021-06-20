FROM python:3.9.5

ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY backup/docker-requirements.txt /code/
RUN pip install -r docker-requirements.txt

COPY . /code/

RUN chmod au+x release
RUN ./release
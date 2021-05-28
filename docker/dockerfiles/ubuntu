# Pull base image
FROM python:3.9.5-buster

# Install psql so that "python manage.py dbshell" works
RUN DEBIAN_FRONTEND=noninteractive apt-get update -qq && apt-get install -y neofetch postgresql-client tidy

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
RUN neofetch
RUN python3 --version

COPY requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt

# Copy project
COPY . /app/
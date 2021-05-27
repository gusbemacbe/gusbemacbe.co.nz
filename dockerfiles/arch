# Pull base image
FROM archlinux/archlinux:latest

# Install psql so that "python manage.py dbshell" works
RUN yes | pacman -Syu

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
RUN yes | pacman -S neofetch postgresql postgresql-libs python python-pip python-psycopg2 python-pytz tidy
RUN neofetch
RUN python --version

COPY requirements.txt /app/requirements.txt
RUN pip install --user -r /app/requirements.txt

# Copy project
COPY . /app/
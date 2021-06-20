# Traditional
# release: chmod au+x release && ./release
# web: gunicorn gusbemacbe.wsgi --log-file -

# Docker
release: chmod au+x release && ./release
web: gunicorn gusbemacbe.wsgi --log-file -
worker: python manage.py rqworker default
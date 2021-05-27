release: python manage.py migrate
web: gunicorn gusbemacbe.wsgi --log-file -
worker: python manage.py rqworker default
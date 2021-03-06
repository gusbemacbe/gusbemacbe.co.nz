"""
Python SECRET_KEY generator.
"""
import random

chars = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!?@#$%^&*()"
size = 50
secret_key = "".join(random.sample(chars, size))

chars = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!?@#$%_"
size = 20
password = "".join(random.sample(chars, size))

CONFIG_STRING = """
DEBUG = True
SECRET_KEY = %s
ALLOWED_HOSTS = *, 127.0.0.1, localhost, localhost:1980, localhost:1984, 0.0.0.0

DATABASE_URL = sqlite:///db.sqlite3
# POSTGRES_DB_URL = postgres://USER:PASSWORD@HOST:PORT/NAME
# POSTGRES_DB = mydb
# POSTGRES_USER = gusbemacbe
# POSTGRES_PASSWORD = %s
# DB_HOST = localhost

# DEFAULT_FROM_EMAIL =
# EMAIL_BACKEND = django.core.mail.backends.smtp.EmailBackend
# EMAIL_HOST = localhost
# EMAIL_PORT =
# EMAIL_HOST_USER =
# EMAIL_HOST_PASSWORD =
# EMAIL_USE_TLS = True
""".strip() % (secret_key, password)

# Writing our configuration file to '.env'
with open('.env', 'w') as configfile:
    configfile.write(CONFIG_STRING)

print('Success!')
print('Type: cat .env')

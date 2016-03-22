# Project and environment specific settings.

PROJECT_ROOT = '/var/www/funcode'

APP_URL = "http://funcode.astrikov.ru"

PORT = 80

DEBUG = False
PRODUCTION = True

DEFAULT_FROM_EMAIL = 'no-reply@astrikov.ru'
EMAIL_HOST = 'localhost'
EMAIL_PORT = 25

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'funcode',
        'USER': 'funcode',
        'PASSWORD': '37FgH1zM',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

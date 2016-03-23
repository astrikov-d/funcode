# Project and environment specific settings.

PROJECT_ROOT = '/var/www/funcode'

APP_URL = "http://funcode.dev:8000"

PORT = 80

DEBUG = True
PRODUCTION = False

DEFAULT_FROM_EMAIL = 'no-reply@funcode.dev'
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'funcode',
        'USER': 'funcode',
        'PASSWORD': 'funcode_pass',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

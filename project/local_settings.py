import os
from settings import BASE_DIR


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'messageboard',
#         'HOST': '127.0.0.1',
#         'USER': 'messageboard',
#         'PASSWORD': 'Grandarcanum7',
#         'PORT': '5432',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite',
    }
}


# http://www.miniwebtool.com/django-secret-key-generator/
SECRET_KEY = 'kbc6p0qdv5!%3y3l&8a+%t%$61v)(jy*@)c$y2!i0jigq&i(cg'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'database.sqlite3'),
#         'HOST': '127.0.0.1',
#         'USER': '',
#         'PASSWORD': '',
#         'PORT': ''
#     }
# }

DEBUG = True

ALLOWED_HOSTS = []

# email settings if you are using gmail
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = ''    # full email address
EMAIL_HOST_PASSWORD = ''    # password of account
EMAIL_USE_TLS = True


from currency_exchange.settings import *

SECRET_KEY = '6$25l)3njoeb84c@$54bd%1bhoz8#al#9v*pc7#(me4)qo1sb='
DEBUG = False
ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

EMAIL_BACKEND = 'django.core.mail.outbox'

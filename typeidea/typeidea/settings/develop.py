from .base import *   #NOQA

ALLOWED_HOSTS = []

DEBUG = True

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'develop.sqlite3'),
	}
} 

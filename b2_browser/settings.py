"""
Django settings for b2_browser project.

Generated by 'django-admin startproject' using Django 3.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qp84-1wae)^)28un&1vklaz*kcwp*@kxyoet%kkx@#xp7_1$cn'

if not DEBUG:
    if 'SECRET_KEY' not in os.environ:
        raise KeyError('SECRET_KEY not set!')
    SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['fdlidx.gflclan.com', 'fastdl.gflclan.com', 'localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'browser.apps.BrowserConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'b2_browser.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'b2_browser.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {}

# Cache

if 'REDIS_URI' not in os.environ:
    cache_uri = 'redis://127.0.0.1:6379/3'
    print(f'Using default redis cache uri {cache_uri}')
else:
    cache_uri = os.environ['REDIS_URI']

if not DEBUG:
    CACHES = {
        "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": cache_uri,
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient",
            }
        }
    }


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = []


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

# Application specific settings

if 'B2_API_ID' not in os.environ or 'B2_API_KEY' not in os.environ or 'B2_BUCKET' not in os.environ or 'CF_ROOT' not in os.environ:
    raise KeyError('Missing one of B2_API_ID, B2_API_KEY, B2_BUCKET, OR CF_ROOT')

B2_API_ID = os.environ['B2_API_ID']
B2_API_KEY = os.environ['B2_API_KEY']
B2_BUCKET = os.environ['B2_BUCKET']
CF_ROOT = os.environ['CF_ROOT']

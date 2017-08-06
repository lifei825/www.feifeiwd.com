"""
Django settings for ffwdsite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""
import pymongo
import os
import sys
from redis import Redis

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
MONGO_URL = os.getenv("MONGO_URL", "mongodb://127.0.0.1:27017")
MYSQL_HOST = os.getenv("MYSQL_HOST", "127.0.0.1")
MYSQL_ROOT_PASSWORD = os.getenv("MYSQL_ROOT_PASSWORD", "")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE", "ffdata")


def redis_conn(db=1):
    # r = Redis(host=REDIS_HOST, port=6379, db=db, password="123)
    r = Redis(host=REDIS_HOST, port=6379, db=db)

    return r

db = pymongo.MongoClient(host=MONGO_URL).ffwd
# db = pymongo.MongoClient(host="mongodb://ffwd:ffwd@127.0.0.1:27017").ffwd
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SESSION_COOKIE_AGE = 3600 * 24 * 10000
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8mjc9mah3uo7187!wwtin!#=$o=*l_8f13ns6sq(-alu6&$r6#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#DEBUG = False

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mydb',
    'mytemp',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'ffwdsite.urls'

WSGI_APPLICATION = 'ffwdsite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': MYSQL_DATABASE,
        'USER': 'root',
        'PASSWORD': MYSQL_ROOT_PASSWORD,
        'HOST': MYSQL_HOST,
        'PORT': '3306',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'utf-8'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_ROOT = os.path.dirname(BASE_DIR) + '/html/static/'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    STATIC_ROOT,
    BASE_DIR + '/img/',
)

TEMPLATE_DIRS = (
    BASE_DIR + '/temp',
)

MEDIA_ROOT = sys.path[0]+'/img'
MEDIA_URL='img/'

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",   
    "django.core.context_processors.debug",          
    "django.core.context_processors.i18n",          
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    'django.core.context_processors.request',     
    'ffwdsite.context_processors.auston_proc',
)


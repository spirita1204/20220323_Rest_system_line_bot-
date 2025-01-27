"""
Django settings for rest_system project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-nx=yxbcsld)nq@g2y973057uxf0)(u22t&o#-vbuw_6pt#d%pp'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'line',
    'cms',
    'shop',
    'payment',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'rest_system.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'rest_system.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

#原本
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  #PostgreSQL
        'NAME': 'DATA_USER',  #資料庫名稱
        'USER': 'postgres',  #資料庫帳號
        'PASSWORD': 'daniel13579',  #資料庫密碼
        'HOST': 'localhost',  #Server(伺服器)位址
        'PORT': '5432'  #PostgreSQL Port號
    }
}
#Heroku使用
'''DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  #PostgreSQL
        'NAME': 'd3011f0hu1ebs',  #資料庫名稱
        'USER': 'wztlbzqjpztlod',  #資料庫帳號
        'PASSWORD': 'a5169d553e3ab681eefd96da7be6b9843f41971ddfe5103cf382e4d3464b58d0',  #資料庫密碼
        'HOST': 'ec2-44-196-223-128.compute-1.amazonaws.com',  #Server(伺服器)位址
        'PORT': '5432'  #PostgreSQL Port號
    }
}'''

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

#
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LINE_CHANNEL_ACCESS_TOKEN = 'X7jiuQZpCGZOzZATX5s2RXwsb156n5l3kMhBcyQOouDXPfu7GLdeRVJ8EcFj2rcG+PthfguopIfQsHqWJbIukIoWoU6xm6jI5/aQqfy53k6FRVsGzPZ4Kol1yc02hL6+zs39JThMG9/eWWvoEY31cQdB04t89/1O/w1cDnyilFU='
LINE_CHANNEL_SECRET = '5554fabd53c745fc880a1d191f87d41e'

EMAIL_ACCOUNT = 'duwu410@gmail.com'
EMAIL_APPLICATION_CODE = 'kitvcbxnnzffzhcg'


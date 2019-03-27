"""
Django settings for ACS project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

from .databases import *
from .application import *
from .i18n import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'xg=d2l0%tt#)uk!j$z%-7hrn=2ipsh0%i*qs6jdc_g6s@eqn!@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

if DEBUG == True:
    ALLOWED_HOSTS = ['localhost', 'it-5', '0.0.0.0', '127.0.0.1', '172.17.66.6']
else:
    ALLOWED_HOSTS = ['localhost', 'it-5', '0.0.0.0', '127.0.0.1', '172.17.66.6']

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'


MEDIA_URL = "/media/"

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    "/home/artem/Dev/Project/LIS/LIS/static",
]

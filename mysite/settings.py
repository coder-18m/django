
"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
from decouple import config

import os
import django_heroku
import dj_database_url



import environ



env = environ.Env()

environ.Env.read_env()



from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')
#SECRET_KEY = "dbcbf480817117b90d296296b42b422412d874236ef22e75"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=bool)
#DEBUG = True

ALLOWED_HOSTS = ['calvsite.herokuapp.com', 'www.contactcalv.org', 'contactcalv.org']


# Application definition

INSTALLED_APPS = [
    'members',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'thesite',
    'ckeditor',
    'django.contrib.auth',
    'cloudinary',
    'cloudinary_storage',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

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

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


#DATABASES = {
#        'default': {
#            'ENGINE': 'django.db.backends.postgresql_psycopg2',
#            'NAME': 'dfqasessl1dib0',
#            'USER': 'uknfqbatvehdrx',
#            'PASSWORD': '8286d7068a5e74e18784b91bb8b735600a458efec69c74ff1ea97e2bb61f7682',
#            'HOST': 'ec2-3-223-169-166.compute-1.amazonaws.com',
#            'PORT': '5432',
#        }
#}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

WHITENOISE_USE_FINDERS = True

# Email settings
# myaccount.google.com/lesssecureapps

#EMAIL_PORT = '587'
#EMAIL_HOST_USER = 'contactCALV@gmail.com'
#EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', 'default')
#EMAIL_USE_TLS = True
# EMAIL_USE_SSL = False

# testing email
#EMAIL_HOST = 'smtp.mailtrap.io'
#EMAIL_HOST_USER = '44f9be80f14246'
#EMAIL_HOST_PASSWORD = 'beab8a86ba2087'
#EMAIL_PORT = '2525'
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_PORT = 587
# EMAIL_HOST = 'smtp-mail.outlook.com'
EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = "calv.official@outlook.com"
EMAIL_HOST_USER = 'calvsite@gmail.com'
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
#EMAIL_HOST_PASSWORD = "nmhyhpphjsoceibo"



# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


LOGIN_REDIRECT_URL = 'home'

LOGOUT_REDIRECT_URL = 'index'

# Cloudinary Storage backend
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'hux9qd4mv',
    'API_KEY': '249675799143621',
    'API_SECRET': config('API_SECRET'),
}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'


# Activate Django-Heroku.
django_heroku.settings(locals())


if os.getcwd() == '/app':
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_SSL_REDIRECT = True

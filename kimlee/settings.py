"""
Django settings for kimlee project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import dropbox
PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT= os.path.join(BASE_DIR,'staticfiles')
STATIC_URL = '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
STATICFILES_DIR= (os.path.join(BASE_DIR,'static'))



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!e$e%sh=%ugt=olfu)cb+z!sgip4bc)7s%iun+l&u-uxsg!ifr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#TEMPLATE_DEBUG = True
DROPBOX_APP_KEY = "08tj7hzyie1k2y7"
DROPBOX_APP_SECRET_KEY = "iqrkzin9rq9smlt"
DROPBOX_APP_ACCESS_TOKEN = "iqrkzin9rq9smlt"
DROPBOX_APP_ACCESS_TOKEN_SECRET = ""

# Optional values below

# The folder where you want the files uploaded.
# Example: /Public or /
DROPBOX_FILE_UPLOAD_FOLDER = ""
# The value below may be either 'app_folder' or 'dropbox'
DROPBOX_ACCESS_TYPE = ""

DEFAULT_FILE_STORAGE = 'storages.backends.dropbox.DropBoxStorage'

dbx = dropbox.Dropbox(DROPBOX_APP_ACCESS_TOKEN)
dbx.users_get_current_account()
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'cart',
    'mathfilters',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
)


ROOT_URLCONF = 'kimlee.urls'


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
            'debug': DEBUG,
        },
    },
]

WSGI_APPLICATION = 'kimlee.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

#DATABASES = {
 #  'default': {
  #     'ENGINE': 'django.db.backends.sqlite3',
   #  'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    #}
#}


DATABASES = { 
     'default':{
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME':'d13poa2htjamoq',
    'USER':'jsfzlktdalbhfz',
    'PASSWORD':'6038bee19d9319c7bb8af5b760b8f4e4fb2ef0acd150dfd12efc151e975881e0',
    'HOST':'ec2-75-101-142-91.compute-1.amazonaws.com',
    'PORT':'5432'

    }
}

#DATABASES = {
    
 #   'default':{
  #  'ENGINE': 'django.db.backends.mysql',
   # 'NAME':'kimlee',
    #'USER':'root',
    #'PASSWORD':'',
    #'HOST':'localhost',
    #'PORT':''

    #}

#}

STATICFILES_STORAGE='whitenoise.storage.CompressedManifestStaticFilesStorage'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

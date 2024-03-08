"""
Django settings for zenhub_project project.

Generated by 'django-admin startproject' using Django 4.2.11.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
import dj_database_url

if os.path.isfile("env.py"):
    import env

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--^1$#wn7*9q+ej$_2)^ibqk^0mdoyh+p((tufjih5h++*3!w4a'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = ['8000-ryanferris7-zenhub-2ncfeobrs30.ws-eu108.gitpod.io', '8000-cianthornhill-zenhub-x9q25lcmnzu.ws-eu108.gitpod.io', '8000-ariannesantiago-zenhub-yf21ouw38kr.ws-eu108.gitpod.io', '8000-tugii21-zenhub-f6emev1j338.ws-eu108.gitpod.io', '.herokuapp.com']



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary_storage',
    'cloudinary',
    'blog',
    'accounts',  # new
    'events',
    'user_profile',
    'links',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'zenhub_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        "DIRS": [
            os.path.join(BASE_DIR, 'templates')
        ],  # new
        #'DIRS': [TEMPLATES_DIR],
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

WSGI_APPLICATION = 'zenhub_project.wsgi.application'


# Database

DATABASES = {
    'default':
    dj_database_url.parse(os.environ.get("DATABASE_URL"))
}



# Old Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
#
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
#    }
#}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# CSRF is required for logging into admin !!!
CSRF_TRUSTED_ORIGINS = [
    "https://*.codeanyapp.com",
    "https://*.herokuapp.com",
    "https://8000-ariannesantiago-zenhub-yf21ouw38kr.ws-eu108.gitpod.io",
    "https://8000-ryanferris7-zenhub-2ncfeobrs30.ws-eu108.gitpod.io",
    "http://8000-ariannesantiago-zenhub-yf21ouw38kr.ws-eu108.gitpod.io",
    "https://8000-cianthornhill-zenhub-x9q25lcmnzu.ws-eu108.gitpod.io",
    "https://8000-tugii21-zenhub-f6emev1j338.ws-eu108.gitpod.io"
]

# django_project/settings.py
LOGIN_REDIRECT_URL = "home"  # new
LOGOUT_REDIRECT_URL = "home"  # new

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend" # new


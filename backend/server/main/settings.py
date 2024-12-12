"""
Django settings for demo project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from dotenv import load_dotenv
from os import getenv
from pathlib import Path
# Load environment variables from .env file
load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = getenv('DEBUG', 'True') == 'True'

# ALLOWED_HOSTS = [
#     'localhost',
#     '127.0.0.1',
#     'server'
# ]
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'rest_framework',
    'rest_framework.authtoken',
    "allauth_ui",
    'allauth',
    'allauth.account',
    'allauth.mfa',
    'allauth.headless',
    'allauth.socialaccount',
    "widget_tweaks",
    "slippers",
    'drf_yasg',
    'corsheaders',
    'adventures',
    'worldtravel',
    'users',
    'django.contrib.gis',
)

MIDDLEWARE = (
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
)

# disable verifications for new users
ACCOUNT_EMAIL_VERIFICATION = 'none'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

# For backwards compatibility for Django 1.8
MIDDLEWARE_CLASSES = MIDDLEWARE

ROOT_URLCONF = 'main.urls'

# WSGI_APPLICATION = 'demo.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': getenv('PGDATABASE'),
        'USER': getenv('PGUSER'),
        'PASSWORD': getenv('PGPASSWORD'),
        'HOST': getenv('PGHOST'),
        'PORT': getenv('PGPORT', 5432),
        'OPTIONS': {
            'sslmode': 'prefer',  # Prefer SSL, but allow non-SSL connections
        },
    }
}



# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/


BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_ROOT = BASE_DIR / "staticfiles"
STATIC_URL = '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
STATICFILES_DIRS = [BASE_DIR / 'static']

STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    }
}


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
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

# Authentication settings

DISABLE_REGISTRATION = getenv('DISABLE_REGISTRATION', 'False') == 'True'
DISABLE_REGISTRATION_MESSAGE = getenv('DISABLE_REGISTRATION_MESSAGE', 'Registration is disabled. Please contact the administrator if you need an account.')

ALLAUTH_UI_THEME = "dark"
SILENCED_SYSTEM_CHECKS = ["slippers.E001"]

AUTH_USER_MODEL = 'users.CustomUser'

ACCOUNT_ADAPTER = 'users.adapters.NoNewUsersAccountAdapter'

ACCOUNT_SIGNUP_FORM_CLASS = 'users.form_overrides.CustomSignupForm'

SESSION_SAVE_EVERY_REQUEST = True

FRONTEND_URL = getenv('FRONTEND_URL', 'http://localhost:3000')

HEADLESS_FRONTEND_URLS = {
    "account_confirm_email": f"{FRONTEND_URL}/user/verify-email/{{key}}",
    "account_reset_password": f"{FRONTEND_URL}/user/reset-password",
    "account_reset_password_from_key": f"{FRONTEND_URL}/user/reset-password/{{key}}",
    "account_signup": f"{FRONTEND_URL}/signup",
    # Fallback in case the state containing the `next` URL is lost and the handshake
    # with the third-party provider fails.
    "socialaccount_login_error": f"{FRONTEND_URL}/account/provider/callback",
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
SITE_ID = 1
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'username'
ACCOUNT_EMAIL_VERIFICATION = 'optional'

if getenv('EMAIL_BACKEND', 'console') == 'console':
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = getenv('EMAIL_HOST')
    EMAIL_USE_TLS = getenv('EMAIL_USE_TLS', 'True') == 'True'
    EMAIL_PORT = getenv('EMAIL_PORT', 587)
    EMAIL_USE_SSL = getenv('EMAIL_USE_SSL', 'False') == 'True'
    EMAIL_HOST_USER = getenv('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = getenv('EMAIL_HOST_PASSWORD')
    DEFAULT_FROM_EMAIL = getenv('DEFAULT_FROM_EMAIL')

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.resend.com'
# EMAIL_USE_TLS = False
# EMAIL_PORT = 2465
# EMAIL_USE_SSL = True
# EMAIL_HOST_USER = 'resend'
# EMAIL_HOST_PASSWORD = ''
# DEFAULT_FROM_EMAIL = 'mail@mail.user.com'


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
}

SWAGGER_SETTINGS = {
    'LOGIN_URL': 'login',
    'LOGOUT_URL': 'logout',
}

CORS_ALLOWED_ORIGINS = [origin.strip() for origin in getenv('CSRF_TRUSTED_ORIGINS', 'http://localhost').split(',') if origin.strip()]


CSRF_TRUSTED_ORIGINS = [origin.strip() for origin in getenv('CSRF_TRUSTED_ORIGINS', 'http://localhost').split(',') if origin.strip()]

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': 'scheduler.log',
        },
    },
    'root': {
        'handlers': ['console', 'file'],
        'level': 'INFO',
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}
# https://github.com/dr5hn/countries-states-cities-database/tags
COUNTRY_REGION_JSON_VERSION = 'v2.4'
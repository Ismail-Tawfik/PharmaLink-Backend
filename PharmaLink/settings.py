"""
Django settings for PharmaLink project.

Generated by 'django-admin startproject' using Django 4.2b1.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

from dotenv import load_dotenv
import os
from pathlib import Path
load_dotenv()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-lz18*w!6o$dojgy#c41&w9!=xfka-bk6h5+w0!f*51i2xlt$oc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework.authtoken',
    'rest_framework',
    'User',
    'Doctor',
    'Prescription',
    'Drugs',
    'drf_spectacular',
    'sslserver',
    'storages',
    'corsheaders',
    'django_seed',
    'django_extensions',
    'django_resized',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.contrib.sessions.middleware.SessionMiddleware',
    # 'django.middleware.security.SecurityMiddleware',
    # 'django_otp.middleware.OTPMiddleware',
    # 'two_factor.middleware.threadlocals.ThreadLocals',
    # 'two_factor.middleware.authy.AuthenticationStatusMiddleware',
    # 'django_otp.middleware.OTPMiddleware',
    # 'django.contrib.auth.middleware.AuthenticationMiddleware',
]

ROOT_URLCONF = 'PharmaLink.urls'

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

WSGI_APPLICATION = 'PharmaLink.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


#Glopal Database
# DATABASES = {
#     'default': {
#         'ENGINE': os.getenv('DB_ENGINE'),
#         'NAME': os.getenv('DB_NAME'),
#         'ENFORCE_SCHEMA': os.getenv('DB_ENFORCE_SCHEMA'),
#         'CLIENT': {
#             'host': os.getenv('DB_CLIENT_HOST')
#         }
#     }
# }

# Local Database
DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DATABASE_ENGINE'),
        'NAME': os.environ.get('DATABASE_NAME'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# LANGUAGE_CODE = os.getenv('LANGUAGE_CODE')
# TIME_ZONE = os.getenv('TIME_ZONE')
# USE_I18N = True
# USE_TZ = True
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/dev/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



# AUTH_USER_MODEL='eventbrit.User'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# AUTH_USER_MODEL='eventbrit.User'
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'django.contrib.auth.backends.ModelBackend',  # default authentication backend
        'User.authentication.CustomTokenAuthentication'
    ],
    # 'DEFAULT_PERMISSION_CLASSES': [
    #     'rest_framework.permissions.IsAuthenticated',
    # ]

}
SPECTACULAR_SETTINGS = {
    'SCHEMA_PATH_FUNC': 'drf_spectacular.views.spectacular_view',
}

# Email settings
# EMAIL_BACKEND = os.getenv('EMAIL_BACKEND')
# EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS')
# EMAIL_HOST = os.getenv('EMAIL_HOST')
# EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
# EMAIL_PORT = os.getenv('EMAIL_PORT')
# EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
# EMAIL_USE_TLS=True


# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# # EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_USE_TLS = True 
# # EMAIL_USE_SSL = True
# # EMAIL_HOST = 'smtp.gmail.com'  # or your SMTP server
# # EMAIL_PORT = 587  # or the appropriate port for your SMTP server
# # EMAIL_HOST_USER = 'pharmalink1190264@gmail.com'
# # EMAIL_HOST_PASSWORD = 'phfn scpq ewst svus'
# # EMAIL_USE_TLS = True
# # EMAIL_PORT = 587
# # EMAIL_HOST='smtp.gmail.com'
# # EMAIL_HOST_USER='eventusmessages@gmail.com'
# # EMAIL_HOST_PASSWORD='msaxsnfytiwwvnbn'
# # EMAIL_PORT=587



# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_USE_TLS = True
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'pharmalink1190264@gmail.com'
# EMAIL_HOST_PASSWORD = 'fvnr dqmh ibta xgax'


# Authentication settings
# AUTH_USER_MODEL = os.getenv('AUTH_USER_MODEL')

AUTH_USER_MODEL = 'User.User'


# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_USE_TLS = False
# EMAIL_USE_SSL = True
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 465  # Use the SSL port
# EMAIL_HOST_USER = 'pharmalink1190264@gmail.com'
# EMAIL_HOST_PASSWORD = 'azuk ngik jmqo udcb'
# SSL_CERTIFICATE = '/Users/ismailtawfik/Documents/GP/PharmaLink/sslserver/certs/development.crt'
# SSL_KEY = '/Users/ismailtawfik/Documents/GP/PharmaLink/sslserver/certs/development.key'


# Use SMTP for sending emails
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# SMTP server settings for Gmail
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587  # Use the TLS port
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False  # Make sure SSL is set to False when using TLS

# Gmail account credentials
MAIL_HOST_USER = 'pharmalink1190264@gmail.com'
EMAIL_HOST_PASSWORD = 'azuk ngik jmqo udcb'

# Default "from" address for emails
DEFAULT_FROM_EMAIL = 'your_default_from_email@example.com'



ALLOWED_HOSTS = ['*']
# SSL_CERTIFICATE = '/etc/letsencrypt/live/event-us.me/fullchain.pem'
# SSL_PRIVATE_KEY = '/etc/letsencrypt/live/event-us.me/privkey.pem'
# # SSL certificate and key files


# Disable SSL verification
# ssl._create_default_https_context = ssl._create_unverified_context
# Authentication settings
# AUTH_USER_MODEL = os.getenv('AUTH_USER_MODEL')

# ALLOWED_HOSTS = ['52.55.220.111']
ALLOWED_HOSTS = ['*']

# Other settings ...

# Use secure cookies
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Redirect all HTTP requests to HTTPS
# SECURE_SSL_REDIRECT = True
# SSL settings
# SSL_CERTIFICATE = os.getenv('SSL_CERTIFICATE')
# SSL_PRIVATE_KEY = os.getenv('SSL_PRIVATE_KEY')
# SSL_CERTIFICATE = '/etc/letsencrypt/live/event-us.me/fullchain.pem'
# SSL_PRIVATE_KEY = '/etc/letsencrypt/live/event-us.me/privkey.pem'

# PASSWORD_RESET_TIMEOUT_DAYS = 7

# MEDIA_URL = '/'
# MEDIA_ROOT = os.path.join(BASE_DIR, '')
# CORS_ORIGIN_ALLOW_ALL = True



# CELERY_BROKER_URL = 'mongodb://localhost:27017/eventbrite'
# CELERY_RESULT_BACKEND = 'mongodb://localhost:27017/eventbrite'
# CELERY_ACCEPT_CONTENT = ['json']
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_SERIALIZER = 'json'



# image resize settings using django_resized
# DJANGORESIZED_DEFAULT_SIZE =os.getenv('DJANGORESIZED_DEFAULT_SIZE')
# DJANGORESIZED_DEFAULT_SCALE = os.getenv('DJANGORESIZED_DEFAULT_SCALE')
# DJANGORESIZED_DEFAULT_QUALITY = os.getenv('DJANGORESIZED_DEFAULT_QUALITY')
# DJANGORESIZED_DEFAULT_KEEP_META = os.getenv('DJANGORESIZED_DEFAULT_KEEP_META')
# DJANGORESIZED_DEFAULT_FORCE_FORMAT = os.getenv('DJANGORESIZED_DEFAULT_FORCE_FORMAT')
# DJANGORESIZED_DEFAULT_FORMAT_EXTENSIONS = os.getenv('DJANGORESIZED_DEFAULT_FORMAT_EXTENSIONS')
# DJANGORESIZED_DEFAULT_NORMALIZE_ROTATION = os.getenv('DJANGORESIZED_DEFAULT_NORMALIZE_ROTATION')

# DJANGORESIZED_DEFAULT_SIZE =[512,256]
# # DJANGORESIZED_DEFAULT_SIZE =[600,300]
# DJANGORESIZED_DEFAULT_SCALE = 1
# DJANGORESIZED_DEFAULT_QUALITY = 75
# DJANGORESIZED_DEFAULT_KEEP_META = True
# DJANGORESIZED_DEFAULT_FORCE_FORMAT = 'JPEG'
# DJANGORESIZED_DEFAULT_FORMAT_EXTENSIONS = {'JPEG': ".jpg"}
# DJANGORESIZED_DEFAULT_NORMALIZE_ROTATION = True

# EMAIL_SSL_CERTFILE = '/etc/letsencrypt/live/event-us.me/fullchain.pem'
# EMAIL_SSL_KEYFILE = '/etc/letsencrypt/live/event-us.me/privkey.pem'



import os

# Set the path to the CA certificate bundle
# SSL_CERT_FILE_PATH = '/etc/ssl/certs/ca-certificates.crt'

# # Set the environment variable
# os.environ['SSL_CERT_FILE'] = SSL_CERT_FILE_PATH

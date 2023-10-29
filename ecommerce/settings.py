"""
Django settings for ecommerce project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import environ
from datetime import timedelta
import os
from django.conf import settings

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(
    # default setting if there not exist
    DEBUG=(bool, True)
)

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

APP_NAME= 'django-ecommerce'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-yor%sow7jfz3fq$=hqs!6fw$vka_y(jd=w=a=3fu8hu746673g'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

ALLOWED_HOSTS = []
APPEND_SLASH = True # use to append slash at end of url with '/' and only wirk with get request, django strict for url and must match on registered routing
# AUTH_USER_MODEL = 'your_app.CustomUser' # when you want to make custom user model and make it as default auth model
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # module
    "master",
    "notification",
    "order",
    "product",
    "store",
    "user",

     # third
    "debug_toolbar",
    "django_extensions",
    "rest_framework",
    "rest_framework.authtoken",
    "rest_framework_simplejwt",
    'rest_framework_simplejwt.token_blacklist',
    "django_seed",
    "safedelete",
    "django_q",
    "clearcache",
    "silk",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # third
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "silk.middleware.SilkyMiddleware",
]

ROOT_URLCONF = 'ecommerce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

FIXTURE_DIRS = [
    BASE_DIR / "master" / "seeder"
]

REST_FRAMEWORK  = {
    'DEFAULT_AUTHENTICATION_CLASSES' : [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication', # this module neeede for default auth djano, in section is django temporray login and logout
        'rest_framework.authentication.TokenAuthentication', # way to know avaible auth type: open https://www.django-rest-framework.org/api-guide/authentication/#setting-the-authentication-scheme and rest_xxx.autxxx.{List of APIReference}
    ],
    'DEFAULT_RENDERER_CLASSES' : [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.IsAuthenticated', # any route who access must login
        'rest_framework.permissions.AllowAny',
    ],
    # https://www.django-rest-framework.org/api-guide/throttling/
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
    ],
    # 'DEFAULT_THROTTLE_RATES': {
    #     'anon': '10000/day', # test for login view
    #     'user': '10000/day',
    #     'login-attempt' : '2/minute', # look user_app.throttling.LoginThrottle
    #     'register-attempt' : '10/minute',
    # },
    # 'TEST_REQUEST_RENDERER_CLASSES': [
    #     # 'rest_framework.renderers.MultiPartRenderer',
    #     'rest_framework.renderers.JSONRenderer',
    #     # 'rest_framework.renderers.TemplateHTMLRenderer'
    # ]

    # for default setting on generic and viewset view, if want on APIView to apply see https://stackoverflow.com/questions/35830779/django-rest-framework-apiview-pagination
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination', # "next": "http://127.0.0.1:8000/watch/stream/review/filter/?limit=4&offset=4&username=admin",
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.CursorPagination', # http://127.0.0.1:8000/watch/stream/review/filter/?cursor=cD0yMDIzLTA3LTIzKzA4JTNBMTIlM0E0Mi44NTg2NzYlMkIwMCUzQTAw&username=admin
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination', # http://127.0.0.1:8000/watch/stream/review/filter/?page=2&username=admin
    # 'PAGE_SIZE': 4
}

# simple jwt will automatic integrated to authorization built-in of django, so you can use basic auth class permission of django directly
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME' : timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME' : timedelta(days=1),
    'ROTATE_REFRESH_TOKENS' : True,
}

WSGI_APPLICATION = 'ecommerce.wsgi.application'

# TEST = {
#     'NAME': 'test_ecommerce_django2'
# }

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('DB_DATABASE'),
        'USER' : env('DB_USERNAME'),
        'PASSWORD' : env('DB_PASSWORD'),
        'STRICT_TRANS_TABLES': True,
        'STRICT_ALL_TABLES': True,
        'sql_mode': 'traditional',
    },
    # 'test' : {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': TEST['NAME'],
    #     'USER' : env('DB_USERNAME'),
    #     'PASSWORD' : env('DB_PASSWORD'),
    #     # 'STRICT_TRANS_TABLES': True,
    #     # 'STRICT_ALL_TABLES': True,
    #     'sql_mode': 'traditional',
    # }
}

CACHES = {
    # "default": {
    #     'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',

    #     # "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
    #     # "LOCATION": "/var/tmp/django_cache",
    # },
    "default" : {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": [
            "redis://127.0.0.1:6379",  # leader
            # "redis://127.0.0.1:6378",  # read-replica 1
            # "redis://127.0.0.1:6377",  # read-replica 2
        ],
        # "OPTIONS": {
        #     "CLIENT_CLASS": "django_redis.client.DefaultClient"
        # },
        "KEY_PREFIX": "dj",
        "TIMEOUT": 60* 15,
    },
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# For django debug toolbar config where he must show
INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]

Q_CLUSTER = {
    'name': 'ecommerce_project',
    'workers': 8,
    'recycle': 500,
    'timeout': 60,
    'compress': True,
    'save_limit': 250,
    'queue_limit': 500,
    'cpu_affinity': 1,
    'label': 'Django Q',
    'cached': 0,

    # 2 drivers can use in same time
    # for now just redis work with auto test
    'redis': {
        'host': '127.0.0.1',
        'port': 6379,
        'db': 0,
    },

    # 'daemonize_workers': False,
    # 'orm': 'default',
    # 'orm': 'default' if settings.TEST else 'test',
    # 'mongo': {
    #         'host': '127.0.0.1',
    #         'port': 27017
    # },
    # 'mongo_db': 'django_q'
}

# print('Q_CLUSTER', Q_CLUSTER['orm'])

# EMAIL
EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST=env('EMAIL_HOST')
EMAIL_PORT=env('EMAIL_PORT')
EMAIL_HOST_USER=env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD=env('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS=env('EMAIL_USE_TLS')
EMAIL_FROM_ADDRESS=env('EMAIL_FROM_ADDRESS')
EMAIL_FROM_NAME=env('EMAIL_FROM_NAME')


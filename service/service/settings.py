from datetime import timedelta
from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-r&o3n5bll$%73xh@k^!3)wflu)n(98-3q)(i%5o1629q(ykj#n'

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
    'rest_framework',

    'rest_framework.authtoken',
    'djoser',
    "corsheaders",


    'cachalot',

    'clients',
    'services',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'service.urls'

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

WSGI_APPLICATION = 'service.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.environ.get('DB_HOST'),
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASS'),
    }
}
#login and password
#admin
#arik1987


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

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
#
REST_FRAMEWORK = {
#     'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
#     'PAGE_SIZE': 2,
#
#
     'DEFAULT_RENDERER_CLASSES': [
         'rest_framework.renderers.JSONRenderer',
         'rest_framework.renderers.BrowsableAPIRenderer'
     ],
#     #'DEFAULT_PERMISSION_CLASSES': [
#      #   'rest_framework.permissions.IsAuthenticated',
#     #],
#
#
#
#
     'DEFAULT_AUTHENTICATION_CLASSES': [
        #'rest_framework.simplejwt.authentication.JWTAuthentication', #jwt
         'rest_framework.authentication.TokenAuthentication',
         'rest_framework.authentication.BasicAuthentication',
         'rest_framework.authentication.SessionAuthentication',
     ]
}
#SIMPLE_JWT = {
 #   "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5), #время жизни
  #  "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
   # "ROTATE_REFRESH_TOKENS": False,
    #"BLACKLIST_AFTER_ROTATION": False,
    #"UPDATE_LAST_LOGIN": False,

    #"ALGORITHM": "HS256",                   #алгоритм шифрования
    #"SIGNING_KEY": SECRET_KEY,
    #"VERIFYING_KEY": "",
    #"AUDIENCE": None,
    #"ISSUER": None,
    #"JSON_ENCODER": None,
    #"JWK_URL": None,
    #"LEEWAY": 0,

    #"AUTH_HEADER_TYPES": ("Bearer",),
    #"AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    #"USER_ID_FIELD": "id",
    #"USER_ID_CLAIM": "user_id",
    #"USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",

    #"AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    #"TOKEN_TYPE_CLAIM": "token_type",
    #"TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",

    #"JTI_CLAIM": "jti",

    #"SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    #"SLIDING_TOKEN_LIFETIME": timedelta(minutes=15),
    #"SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),

    #"TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainPairSerializer",
    #"TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSerializer",
    #"TOKEN_VERIFY_SERIALIZER": "rest_framework_simplejwt.serializers.TokenVerifySerializer",
    #"TOKEN_BLACKLIST_SERIALIZER": "rest_framework_simplejwt.serializers.TokenBlacklistSerializer",
    #"SLIDING_TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainSlidingSerializer",
    #"SLIDING_TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSlidingSerializer",
#}

#
DJOSER = {
     'PASSWORD_RESET_CONFIRM_URL': '#/password/reset/confirm/{uid}/{token}',
     'USERNAME_RESET_CONFIRM_URL': '#/username/reset/confirm/{uid}/{token}',
     'ACTIVATION_URL': '#/activate/{uid}/{token}',
     'SEND_ACTIVATION_EMAIL': True,
     'SERIALIZERS': {},
}




DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


LOGGING = {
    'version': 1,
    'handlers': {
        'console': {'class': 'logging.StreamHandler'}
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG'
        }
    }
}


CELERY_BROKER_URL = 'redis://redis:6379/0'


CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://redis:6379/1',

    }
}


PRICE_CACHE_NAME = 'price_cache'


CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
    "http://127.0.0.1:8000",
]

CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]
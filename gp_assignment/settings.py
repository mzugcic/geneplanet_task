import os

from configurations import Configuration, values


class Base(Configuration):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DOTENV = os.path.join(BASE_DIR, '.env')

    DEBUG = values.BooleanValue(False)
    SECRET_KEY = values.SecretValue()
    ALLOWED_HOSTS = values.ListValue([])

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'genomes',
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

    ROOT_URLCONF = 'gp_assignment.urls'

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

    WSGI_APPLICATION = 'gp_assignment.wsgi.application'

    DATABASES = values.DatabaseURLValue()

    AUTH_PASSWORD_VALIDATORS = [
        {
            'NAME': 'django.contrib.auth.password_validation.'
            'UserAttributeSimilarityValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.'
            'MinimumLengthValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.'
            'CommonPasswordValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.'
            'NumericPasswordValidator',
        },
    ]

    LANGUAGE_CODE = 'en-us'
    USE_I18N = True
    USE_L10N = True

    TIME_ZONE = 'UTC'
    USE_TZ = True
    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework.authentication.SessionAuthentication',
        ),
    }

    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')


class Dev(Base):
    DEBUG = values.BooleanValue(True)
    ALLOWED_HOSTS = values.ListValue(['localhost', '127.0.0.1'])

    MIDDLEWARE = [
        'debug_toolbar.middleware.DebugToolbarMiddleware'
    ] + Base.MIDDLEWARE

    INSTALLED_APPS = Base.INSTALLED_APPS + [
        'debug_toolbar',
    ]

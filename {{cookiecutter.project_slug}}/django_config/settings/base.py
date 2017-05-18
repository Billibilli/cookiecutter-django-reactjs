"""
Django settings for {{cookiecutter.project_name}} project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""
import datetime
import environ

ROOT_DIR = environ.Path(__file__) - 3  # ({{ cookiecutter.project_slug }}/django_config/settings/base.py - 3 = {{ cookiecutter.project_slug }}/)
APPS_DIR = ROOT_DIR.path('{{ cookiecutter.project_slug }}')

# Load operating system environment variables and then prepare to use them
env = environ.Env()

# .env file, should load only in development environment
READ_DOT_ENV_FILE = env.bool('DJANGO_READ_DOT_ENV_FILE', default=False)

if READ_DOT_ENV_FILE:
    # Operating System Environment variables have precedence over variables defined in the .env file,
    # that is to say variables from the .env files will only be used if not defined
    # as environment variables.
    env_file = str(ROOT_DIR.path('.env'))
    print('Loading : {}'.format(env_file))
    env.read_env(env_file)
    print('The .env file has been loaded. See base.py for more information')

# APP CONFIGURATION
# ------------------------------------------------------------------------------
DJANGO_APPS = [
    # Default Django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Useful template tags:
    # 'django.contrib.humanize',

    # Admin
    'django.contrib.admin',
]
THIRD_PARTY_APPS = [
    'crispy_forms',  # Form layouts
    'allauth',  # registration
    'allauth.account',  # registration
    'allauth.socialaccount',  # registration

    'django_python3_ldap',  # LDAP authentication: https://github.com/etianen/django-python3-ldap
    'oauth2_provider',  # OAUTH2: https://github.com/evonove/django-oauth-toolkit/tree/master/oauth2_provider

    # Django REST framework: http://www.django-rest-framework.org/#installation
    'rest_framework',
    'rest_framework.authtoken',

    # Django REST Auth: https://github.com/Tivix/django-rest-auth
    'rest_auth',
    'rest_auth.registration',

    # Swagger: https://github.com/marcgibbons/django-rest-swagger/tree/master/rest_framework_swagger
    'rest_framework_swagger',

    # Webpack Loader: https://github.com/owais/django-webpack-loader
    'webpack_loader',

    # CORS HEADERS: https://github.com/ottoyiu/django-cors-headers
    'corsheaders',  # Allows us to easily manipulate CORS settings

]

# Apps specific for this project go here.
LOCAL_APPS = [
    # custom users app
    '{{ cookiecutter.project_slug }}.users.apps.UsersConfig',
    # Your stuff: custom apps go here
]

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# SITE CONFIGURATION
# ------------------------------------------------------------------------------
# Hosts/domain names that are valid for this site
# See https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default=['{{cookiecutter.domain_name}}', '.127.0.0.1', '.0.0.0.0'])

# MIDDLEWARE CONFIGURATION
# ------------------------------------------------------------------------------
SECURITY_MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
]

# This is required to go first! See: https://github.com/ottoyiu/django-cors-headers#setup
CORS_MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
]

DJANGO_MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

MIDDLEWARE = SECURITY_MIDDLEWARE + CORS_MIDDLEWARE + DJANGO_MIDDLEWARE

# MIGRATIONS CONFIGURATION
# ------------------------------------------------------------------------------
MIGRATION_MODULES = {
    'sites': '{{ cookiecutter.project_slug }}.contrib.sites.migrations'
}

# DEBUG
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env.bool('DJANGO_DEBUG', False)

# FIXTURE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-FIXTURE_DIRS
FIXTURE_DIRS = (
    str(APPS_DIR.path('fixtures')),
)

# EMAIL CONFIGURATION
# ------------------------------------------------------------------------------
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND', default='django.core.mail.backends.smtp.EmailBackend')

# MANAGER CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = [
    ("""{{cookiecutter.author_name}}""", '{{cookiecutter.email}}'),
]

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS

# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': env.db('DATABASE_URL', default='postgres://{% if cookiecutter.windows == 'y' %}localhost{% endif %}/{{cookiecutter.project_slug}}'),
}
DATABASES['default']['ATOMIC_REQUESTS'] = True


# GENERAL CONFIGURATION
# ------------------------------------------------------------------------------
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = '{{ cookiecutter.timezone }}'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = 'en-us'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True

# TEMPLATE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        # See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATES-BACKEND
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
        'DIRS': [
            str(APPS_DIR.path('templates')),
        ],
        'OPTIONS': {
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
            'debug': DEBUG,
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
            # https://docs.djangoproject.com/en/dev/ref/templates/api/#loader-types
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                # Your stuff: custom template context processors go here
            ],
        },
    },
]

# See: http://django-crispy-forms.readthedocs.io/en/latest/install.html#template-packs
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# STATIC FILE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = str(ROOT_DIR('staticfiles'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/static/'

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = [
    str(APPS_DIR.path('static')),
    str(ROOT_DIR.path('frontend')),
]

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# MEDIA CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = str(APPS_DIR('media'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'

# URL Configuration
# ------------------------------------------------------------------------------
ROOT_URLCONF = 'django_config.urls'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = 'django_config.wsgi.application'

# PASSWORD STORAGE SETTINGS
# ------------------------------------------------------------------------------
# See https://docs.djangoproject.com/en/dev/topics/auth/passwords/#using-argon2-with-django
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
]

# PASSWORD VALIDATION
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators
# ------------------------------------------------------------------------------

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

# AUTHENTICATION CONFIGURATION
# ------------------------------------------------------------------------------
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',

    # Python3-LDAP
    # See: https://github.com/etianen/django-python3-ldap#installation
    'django_python3_ldap.auth.LDAPBackend',

    # Django allauth
    # See: http://django-allauth.readthedocs.io/en/latest/installation.html#django
    'allauth.account.auth_backends.AuthenticationBackend',
]

# Some really nice defaults
ACCOUNT_AUTHENTICATION_METHOD = 'username'
ACCOUNT_EMAIL_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_UNIQUE_EMAIL = True

ACCOUNT_ALLOW_REGISTRATION = env.bool('DJANGO_ACCOUNT_ALLOW_REGISTRATION', True)
ACCOUNT_ADAPTER = '{{cookiecutter.project_slug}}.users.adapters.AccountAdapter'
SOCIALACCOUNT_ADAPTER = '{{cookiecutter.project_slug}}.users.adapters.SocialAccountAdapter'

# Custom user app defaults
# Select the correct user model
AUTH_USER_MODEL = 'users.User'
LOGIN_REDIRECT_URL = 'users:redirect'
LOGIN_URL = 'account_login'

# SLUGLIFIER
AUTOSLUG_SLUGIFY_FUNCTION = 'slugify.slugify'
{% if cookiecutter.use_celery == 'y' %}
########## CELERY
INSTALLED_APPS += ['{{cookiecutter.project_slug}}.taskapp.celery.CeleryConfig']
CELERY_BROKER_URL = env('CELERY_BROKER_URL', default='django://')
if CELERY_BROKER_URL == 'django://':
    CELERY_RESULT_BACKEND = 'redis://'
else:
    CELERY_RESULT_BACKEND = CELERY_BROKER_URL
########## END CELERY
{% endif %}

{%- if cookiecutter.use_compressor == 'y'-%}
# django-compressor
# ------------------------------------------------------------------------------
INSTALLED_APPS += ['compressor']
STATICFILES_FINDERS += ['compressor.finders.CompressorFinder']
{%- endif %}

# Location of root django.contrib.admin URL, use {% raw %}{% url 'admin:index' %}{% endraw %}
ADMIN_URL = r'^admin/'

# Your common stuff: Below this line define 3rd party library settings
# ------------------------------------------------------------------------------


# DJANGO REST FRAMEWORK
# ------------------------------------------------------------------------------
# http://www.django-rest-framework.org/

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        # 'rest_framework.authentication.TokenAuthentication',

        # For Django-oauth. See: https://django-oauth-toolkit.readthedocs.io/en/latest/rest-framework/getting_started.html#step-1-minimal-setup  # NOQA
        'oauth2_provider.ext.rest_framework.OAuth2Authentication',

        # For REST-JWT. See: http://getblimp.github.io/django-rest-framework-jwt/#usage
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 250,
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
    'COERCE_DECIMAL_TO_STRING': False,
}

# Swagger API CONFIGURATION
# ------------------------------------------------------------------------------
# https://marcgibbons.github.io/django-rest-swagger/settings/

SWAGGER_SETTINGS = {
    'VALIDATOR_URL': None,
    'SHOW_REQUEST_HEADERS': True,
}

# LDAPBackend CONFIGURATION
# ------------------------------------------------------------------------------
# https://github.com/etianen/django-python3-ldap

LDAP_AUTH_URL = env('LDAP_AUTH_URL', default='update')

LDAP_AUTH_CONNECTION_USERNAME = env(
    'LDAP_AUTH_CONNECTION_USERNAME',
    default='update'
)

LDAP_AUTH_CONNECTION_PASSWORD = env('LDAP_AUTH_CONNECTION_PASSWORD', default='update')

LDAP_AUTH_USE_TLS = env.bool('LDAP_AUTH_USE_TLS', default=False)

LDAP_AUTH_SEARCH_BASE = env('LDAP_AUTH_SEARCH_BASE', default='update')

LDAP_AUTH_OBJECT_CLASS = env('LDAP_AUTH_OBJECT_CLASS', default='update')

LDAP_AUTH_USER_LOOKUP_FIELDS = ('username',)

LDAP_AUTH_FORMAT_USERNAME = 'django_python3_ldap.utils.format_username_active_directory'

LDAP_AUTH_ACTIVE_DIRECTORY_DOMAIN = env('LDAP_AUTH_ACTIVE_DIRECTORY_DOMAIN', default='update')

LDAP_AUTH_USER_FIELDS = env.dict('LDAP_AUTH_USER_FIELDS', default={})

# We can use this to map LDAP attributes to UserProfile
LDAP_AUTH_SYNC_USER_RELATIONS = 'django_python3_ldap.utils.sync_user_relations'

# DJANGO REST-AUTH
# ------------------------------------------------------------------------------
# https://github.com/Tivix/django-rest-auth/

REST_USE_JWT = True

OLD_PASSWORD_FIELD_ENABLED = True

LOGOUT_ON_PASSWORD_CHANGE = True

# DJANGO REST FRAMEWORK JSON WEB TOKEN
# ------------------------------------------------------------------------------
# https://github.com/GetBlimp/django-rest-framework-jwt

JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1),
    'JWT_ALLOW_REFRESH': True,
}

# OAUTH2 CONFIGURATION
# ------------------------------------------------------------------------------
# https://django-oauth-toolkit.readthedocs.io/en/latest/rest-framework/getting_started.html

OAUTH2_PROVIDER = {
    # this is the list of available scopes
    'SCOPES': {
        'read': 'Read scope',
        'write': 'Write scope',
    },
    'ACCESS_TOKEN_EXPIRE_SECONDS': 31536000,  # Sets OAUTH access tokens good for a year
}

# CORS CONFIGURATION
# ------------------------------------------------------------------------------
# https://github.com/ottoyiu/django-cors-headers#configuration
CORS_ORIGIN_ALLOW_ALL = True

# LOGGING CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s '
                      '%(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': env('DJANGO_LOG_LEVEL', default='DEBUG'),
        },
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console', ],
            'propagate': False,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True
        },
        'django.security.DisallowedHost': {
            'level': 'ERROR',
            'handlers': ['console', 'mail_admins'],
            'propagate': True
        },
        "django_python3_ldap": {
            "handlers": ["console"],
            "level": "INFO",
        },
    }
}

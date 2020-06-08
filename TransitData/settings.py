"""
Django settings for TransitData project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

from celery.schedules import crontab

MODE = "dev"  #could be prod, dev, test

if MODE == "prod":
    DEBUG = False
    ALLOWED_HOSTS = ['publictransportationportal.azurewebsites.net']
    db_USER = os.environ.get("db_USER")
    db_PASSWORD = os.environ.get("db_PASSWORD")
    SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')
    os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')
    #SAML Config
    ASSERTION_URL = "https://publictransportationportal.azurewebsites.net"
    ENTITY_ID = "https://publictransportationportal.azurewebsites.net"
    METADATA_LOCAL_FILE_PATH = '/usr/bin/sawidp_WaTech_metadata_PROD.xml'
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SEND_EMAILS = True
elif MODE == "test":
    DEBUG = True
    ALLOWED_HOSTS = ['*']
    db_USER = os.environ.get("db_USER")
    db_PASSWORD = os.environ.get("db_PASSWORD")
    SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')
    os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')
    ASSERTION_URL = "https://vanpooldev.azurewebsites.net"
    ENTITY_ID = "https://vanpooldev.azurewebsites.net"
    METADATA_LOCAL_FILE_PATH = '/usr/bin/sawidp_WaTech_metadata_TEST.xml'
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SEND_EMAILS = False
elif MODE == "dev":
    DEBUG = True
    ALLOWED_HOSTS = ['*']
    import keys_and_passwords
    db_USER = keys_and_passwords.db_USER
    db_PASSWORD = keys_and_passwords.db_PASSWORD
    SENDGRID_API_KEY = keys_and_passwords.SENDGRID_API_KEY
    ASSERTION_URL = "https://vanpooldev.azurewebsites.net"
    ENTITY_ID = "https://vanpooldev.azurewebsites.net"
    METADATA_LOCAL_FILE_PATH = '/usr/bin/sawidp_WaTech_metadata_TEST.xml'
    SECRET_KEY = 'x%b_yxu0_1k3i9t$e&yr0h)edaj0u07hp+dg(&yy^m28x2zkmo'
    SEND_EMAILS = False
else:
    raise NotImplementedError()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# if mode:
#     STATIC_URL = '/static/'
#     STATIC_ROOT = os.path.join(BASE_DIR, "static")
#     STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# else:
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/


# Application definition

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'bootstrap4',
    'phonenumber_field',
    'localflavor',
    'mailer',
    'widget_tweaks',
    'django.contrib.humanize',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Panacea.apps.PanaceaConfig',
    'django.forms',
    'django_filters',
    'simple_history',
    'django_celery_beat',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'ckeditor',
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
    'simple_history.middleware.HistoryRequestMiddleware',
]

EMAIL_BACKEND = 'sgbackend.SendGridBackend'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'ptreportingportal@wsdot.wa.gov'

ROOT_URLCONF = 'TransitData.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

FORM_RENDERER = 'django.forms.renderers.TemplatesSetting'

LOGIN_REDIRECT_URL = 'dashboard'
LOGOUT_REDIRECT_URL = '/Panacea/login'

WSGI_APPLICATION = 'TransitData.wsgi.application'

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.PanaceaDB'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': 'PublicTransportationDataReportingPortal',
        'HOST': 'hqcw2sql01.database.windows.net',
        'USER': db_USER,
        'PASSWORD': db_PASSWORD,
        'PORT': '',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
        },
    }
}

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

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/




# User authentication from tut located here:https://wsvincent.com/django-custom-user-model-tutorial/

AUTH_USER_MODEL = 'Panacea.custom_user'

ENABLE_PERMISSIONS = True

PHONENUMBER_DEFAULT_REGION = 'US'

CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'

CELERY_BEAT_SCHEDULE = {'send_emails_now': {'task': 'Panacea.tasks.send_emails_now',
                                            'schedule': crontab(minute="*")}

                        }

MEDIA_ROOT = '/var/media/'
MEDIA_URL = '/media/'

# SAML Settings for WSDOT employees - Azure
SAML2_AUTH = {
    # Metadata is required, choose either remote url or local file path
    'METADATA_AUTO_CONF_URL': 'https://login.microsoftonline.com/6f10858a-931e-4554-89f7-a3694e8e0f1a/federationmetadata/2007-06/federationmetadata.xml?appid=666dd47c-2480-4ffa-b3ce-37f1cd37051c ',
    # 'METADATA_LOCAL_FILE_PATH': '[The metadata configuration file path]',

    # Optional settings below
    'DEFAULT_NEXT_URL': '/dashboard',  # Custom target redirect URL after the user get logged in. Default to /admin if not set. This setting will be overwritten if you have parameter ?next= specificed in the login URL.
    'CREATE_USER': 'FALSE', # Create a new Django user when a new user logs in. Defaults to True.
    'NEW_USER_PROFILE': {
        'USER_GROUPS': [],  # The default group name when a new user logs in
        'ACTIVE_STATUS': True,  # The default active status for new users
        'STAFF_STATUS': False,  # The staff status for new users
        'SUPERUSER_STATUS': False,  # The superuser status for new users
    },
    'ATTRIBUTES_MAP': {  # Change Email/UserName/FirstName/LastName to corresponding SAML2 userprofile attributes.
        'email': 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress',
        'username': 'http://schemas.microsoft.com/identity/claims/displayname',
        'first_name': 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/givenname',
        'last_name': 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/surname',
    },
    'TRIGGER': {
        # 'CREATE_USER': 'path.to.your.new.user.hook.method',
        # 'BEFORE_LOGIN': 'path.to.your.login.hook.method',
    },
    'ASSERTION_URL': ASSERTION_URL + '/sso/wsdot/reply', # Custom URL to validate incoming SAML requests against
    'ENTITY_ID': ENTITY_ID + '/sso/wsdot/', # Populates the Issuer element in authn request
    'NAME_ID_FORMAT': 'urn:oasis:names:tc:SAML:2.0:nameid-format:persistent', # Sets the Format property of authn NameIDPolicy element
    'USE_JWT': False, # Set this to True if you are running a Single Page Application (SPA) with Django Rest Framework (DRF), and are using JWT authentication to authorize client users
    'FRONTEND_URL': '', # Redirect URL for the client if you are using JWT auth with DRF. See explanation below
}

# SAML Settings for external users - SAW
SAML2_AUTH_SAW = {
    # Metadata is required, choose either remote url or local file path
    # 'METADATA_AUTO_CONF_URL': 'https://login.microsoftonline.com/6f10858a-931e-4554-89f7-a3694e8e0f1a/federationmetadata/2007-06/federationmetadata.xml?appid=666dd47c-2480-4ffa-b3ce-37f1cd37051c ',
    'METADATA_LOCAL_FILE_PATH': METADATA_LOCAL_FILE_PATH,

    # Optional settings below
    'DEFAULT_NEXT_URL': '/dashboard',  # Custom target redirect URL after the user get logged in. Default to /admin if not set. This setting will be overwritten if you have parameter ?next= specificed in the login URL.
    'CREATE_USER': 'TRUE', # Create a new Django user when a new user logs in. Defaults to True.
    'NEW_USER_PROFILE': {
        'USER_GROUPS': [],  # The default group name when a new user logs in
        'ACTIVE_STATUS': True,  # The default active status for new users
        'STAFF_STATUS': False,  # The staff status for new users
        'SUPERUSER_STATUS': False,  # The superuser status for new users
    },
    'ATTRIBUTES_MAP': {  # Change Email/UserName/FirstName/LastName to corresponding SAML2 userprofile attributes.
        'saw_id': 'guid',
        'email': 'email',
        'username': 'user',
        'full_name': 'name',
    },
    'TRIGGER': {
        # 'CREATE_USER': 'path.to.your.new.user.hook.method',
        # 'BEFORE_LOGIN': 'path.to.your.login.hook.method',
    },
    'ASSERTION_URL': ASSERTION_URL + '/sso/saw/acs', # Custom URL to validate incoming SAML requests against
    'ENTITY_ID': ENTITY_ID + '/sso/saw/', # Populates the Issuer element in authn request
    'NAME_ID_FORMAT': 'urn:oasis:names:tc:SAML:2.0:nameid-format:persistent', # Sets the Format property of authn NameIDPolicy element
    'USE_JWT': False, # Set this to True if you are running a Single Page Application (SPA) with Django Rest Framework (DRF), and are using JWT authentication to authorize client users
    'FRONTEND_URL': '', # Redirect URL for the client if you are using JWT auth with DRF. See explanation below
}

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Basic',
        'toolbar_Basic': [
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList',],
            ['Link',],
        ],
        'height': 100,
        'width': '100%',
        'removePlugins': 'elementspath',
        'linkShowAdvancedTab': False,
        'linkShowTargetTab': False,
    }
}
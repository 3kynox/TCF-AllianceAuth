# Every setting in base.py can be overloaded by redefining it here.
import os
from dotenv import load_dotenv
from .base import *

env_path = '/home/allianceserver/TCF/.env'
load_dotenv(env_path)

if not os.getenv('DB_PASSWORD'):
    raise ValueError("Environment varibales not loaded ! Please verify file .env")

# These are required for Django to function properly. Don't touch.
ROOT_URLCONF = 'TCF.urls'
WSGI_APPLICATION = 'TCF.wsgi.application'
SECRET_KEY = os.getenv('SECRET_KEY')

# This is where css/images will be placed for your webserver to read
STATIC_ROOT = "/var/www/TCF/static/"

# Change this to change the name of the auth site displayed
# in page titles and the site header.
SITE_NAME = 'TCF - Tau Ceti Federation'

# This is your websites URL, set it accordingly
# Make sure this URL is WITHOUT a trailing slash
SITE_URL = "https://taucetifederation.space"

# Django security
CSRF_TRUSTED_ORIGINS = [SITE_URL]

# Change this to enable/disable debug mode, which displays
# useful error messages but can leak sensitive data.
DEBUG = True

# Add any additional apps to this list.
INSTALLED_APPS += [
    #'allianceauth.theme.bootstrap',
    'allianceauth.services.modules.discord',
]

# To change the logging level for extensions, uncomment the following line.
# LOGGING['handlers']['extension_file']['level'] = 'DEBUG'

# By default, apps are prevented from having public views for security reasons.
# To allow specific apps to have public views, add them to APPS_WITH_PUBLIC_VIEWS
#   » The format is the same as in INSTALLED_APPS
#   » The app developer must also explicitly allow public views for their app
APPS_WITH_PUBLIC_VIEWS = [

]

# Enter credentials to use MySQL/MariaDB. Comment out to use sqlite3
DATABASES['default'] = {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'alliance_auth',
    'USER': os.getenv('DB_USER'),
    'PASSWORD': os.getenv('DB_PASSWORD'),
    'HOST': '127.0.0.1',
    'PORT': '3306',
    'OPTIONS': {'charset': 'utf8mb4'},
}

# Register an application at https://developers.eveonline.com for Authentication
# & API Access and fill out these settings. Be sure to set the callback URL
# to https://example.com/sso/callback substituting your domain for example.com in
# CCP's developer portal
# Logging in to auth requires the publicData scope (can be overridden through the
# LOGIN_TOKEN_SCOPES setting). Other apps may require more (see their docs).
ESI_SSO_CLIENT_ID = os.getenv('ESI_SSO_CLIENT_ID')
ESI_SSO_CLIENT_SECRET = os.getenv('ESI_SSO_CLIENT_SECRET')
ESI_SSO_CALLBACK_URL = "https://taucetifederation.space/sso/callback/"
ESI_USER_CONTACT_EMAIL = os.getenv('ESI_USER_CONTACT_EMAIL')
ESI_SSO_URL = "https://login.eveonline.com/v2/oauth"
ESI_API_URL = "https://esi.evetech.net"

# By default, emails are validated before new users can log in.
# It's recommended to use a free service like SparkPost or Elastic Email to send email.
# https://www.sparkpost.com/docs/integrations/django/
# https://elasticemail.com/resources/settings/smtp-api/
# Set the default from email to something like 'noreply@example.com'
# Email validation can be turned off by uncommenting the line below. This can break some services.
# REGISTRATION_VERIFY_EMAIL = False
TEMPLATES[0]['DIRS'].insert(0, '/home/allianceserver/TCF/TCF/templates')
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_PORT = 25
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False
EMAIL_USE_SSL = False
DEFAULT_FROM_EMAIL = 'root@kernelpanik.fr'
SERVER_EMAIL = 'kp@kernelpanik.fr'
ADMINS = [('Admin', 'root@kernelpanik.fr')]
SITE_NAME = 'Tau Ceti Federation'
ALLIANCE_AUTH_SITE_NAME = 'Portail Tau Ceti Federation (TCF)'
EMAIL_MULTIPART_ALTERNATIVES = True

# Cache compression can help on bigger auths where ram starts to become an issue.
# Uncomment the following 3 lines to enable.

#CACHES["default"]["OPTIONS"] = {
#    "COMPRESSOR": "django_redis.compressors.lzma.LzmaCompressor",
#}

#######################################
# Add any custom settings below here. #
#######################################

# Configuration des sessions
SESSION_ENGINE = 'django.contrib.sessions.backends.db'
SESSION_COOKIE_SECURE = True  # Parce que vous utilisez HTTPS
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = 'Lax'
SESSION_COOKIE_NAME = 'allianceauth_sessionid'
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_COOKIE_AGE = 3600 * 24 * 7  # 7 jours

# Configuration CSRF pour HTTPS
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_SAMESITE = 'Lax'
CSRF_TRUSTED_ORIGINS = [
    'https://taucetifederation.space',
    'https://www.taucetifederation.space',
]

# Configuration Discord
DISCORD_GUILD_ID = os.getenv('DISCORD_GUILD_ID')
DISCORD_CALLBACK_URL = f"{SITE_URL}/discord/callback/"
DISCORD_APP_ID = os.getenv('DISCORD_APP_ID')
DISCORD_APP_SECRET = os.getenv('DISCORD_APP_SECRET')
DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
DISCORD_SYNC_NAMES = False

CELERYBEAT_SCHEDULE['discord.update_all_usernames'] = {
    'task': 'discord.update_all_usernames',
    'schedule': crontab(minute='0', hour='*/12'),
}

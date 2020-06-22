from .base import *

DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1']

INSTALLED_APPS += [
    'debug_toolbar',
    'fcm_django',
    'push_notifications'
]

PUSH_NOTIFICATIONS_SETTINGS = {
        "FCM_API_KEY": "AAAAP-ISdnI:APA91bGc_D_sTTZrlfO6sgqQOiAYt7_KuXipDW64fdCLIPIV1wnQnvg9j5mpCH5COmrT1IQ6VMq3uF6XqHMuMnRgm9x9VdkchTuu2BKhbOfoRECkW__afMi24L90IllKXAChtZOiugfB",
        "APNS_CERTIFICATE": os.path.join(BASE_DIR, "public_key.pem"),
        "APNS_TOPIC": "127.0.0.1",
        "WP_PRIVATE_KEY": os.path.join(BASE_DIR, "private_key.pem"),
        "WP_CLAIMS": {"sub": "mailto: development@example.com"}
}

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]

# DEBUG TOOLBAR SETTINGS

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]


def show_toolbar(request):
    return True


DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TOOLBAR_CALLBACK': show_toolbar
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STRIPE_PUBLIC_KEY = ''
STRIPE_SECRET_KEY = ''

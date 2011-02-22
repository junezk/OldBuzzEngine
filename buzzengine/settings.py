import os

DEBUG = True
ROOT_PATH = os.path.dirname(__file__)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
)
INSTALLED_APPS = (
    'buzzengine.api',
)
TEMPLATE_DIRS = (
    os.path.join(ROOT_PATH, 'templates'),
)
ROOT_URLCONF = 'buzzengine.urls'
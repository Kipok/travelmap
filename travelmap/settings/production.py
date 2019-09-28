"""Production django settings"""

from travelmap.settings.base import *


DEBUG = False
ALLOWED_HOSTS = ['travel.igitman.com', 'www.travel.igitman.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {'read_default_file': os.path.join(BASE_DIR, 'db.conf'),
                    'charset': 'utf8mb4'},
        'HOST': 'localhost',
        'PORT': '',
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': '../logs/django.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'WARNING',
            'propagate': True,
        },
    },
}

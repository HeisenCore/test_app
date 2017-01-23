# coding: utf-8

import os
import logging

APP_NAME = 'test'

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

INSTANCE_COUNT = 1

VALIDATOR_CLASS = 'libs.validator.CustomValidator'

DATABASES = {
    'test': {
        'host': '192.168.0.210',
        'port': 27017,
        'db': 'test_db',
        'log_query': False,
        'log_query_data': False,
        'log_results': False,
    },
}

AP_DATABASE = 'test'

LOGGERS = {
    'test_log': {
        'format': 'basic',
        'level': logging.DEBUG
    },
}

EMAIL_TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
EMAIL_BACKEND = 'debug'         # shoud be either debug or smtp
# EMAIL_HOST = 'mail.airport.ir'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'fidsthr'
# EMAIL_HOST_PASSWORD = '1nfids1394'

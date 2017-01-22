# coding: utf-8

import os

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

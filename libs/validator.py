import datetime

from heisen.core.validator.validator import Validator


class CustomValidator(Validator):
    def _validate_type_datetime(self, value):
        if isinstance(value, datetime.datetime):
            return True

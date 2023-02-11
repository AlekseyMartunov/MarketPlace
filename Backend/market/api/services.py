from copy import deepcopy
import functools

from rest_framework import serializers


# {
#     "name": "new Name 33jgkflf3",
#     "description": "1",
#     "amount": 300,
#     "params": {
#         "type": "some_text",
#         "mass": 500,
#         "price": "some string",
#         "color": true
#     },
#     "category": 1
# }

class OnlyAllowedParams:
    """
     Базовый класс для проверки данных jsonField
    """
    def __init__(self, validate_field: str):
        self._key = validate_field
        self._allowed_params = None

    def __call__(self, *args, **kwargs):
        raise "This method should be overridden"

    def _get_validated_data(self, not_valid_data: dict) -> dict:
        date = deepcopy(not_valid_data)
        validated = self._validate_data(date[self._key])
        date.pop(self._key)
        date.setdefault(self._key, validated)
        return date

    def _validate_data(self, data: dict) -> dict:
        val_keys = self._validate_keys(data)
        self._validate_values(val_keys)
        return val_keys

    def _validate_keys(self, data: dict) -> dict:
        val_data = {key: value for key, value in data.items() if key in self._allowed_params.keys()}

        if len(val_data) < len(self._allowed_params):
            empty_keys = set(self._allowed_params.keys()).difference(val_data.keys())
            raise serializers.ValidationError(f"In params missing keys {empty_keys}")
        return val_data

    def _validate_values(self, data: dict):
        types_dict = {
            'number': int,
            'string': str,
            'bool': bool,
        }

        for key, value in self._allowed_params.items():
            if types_dict[value] != type(data[key]):
                raise serializers.ValidationError(f"Type {key} must be {value}")

    def _set_allowed_params(self, data: dict):
        self._allowed_params = data.get('category').allowed_params[self._key]


class OnlyAllowedParamsCreate(OnlyAllowedParams):
    def __call__(self, func, *args, **kwargs):
        @functools.wraps(func)
        def decorated(paren_class, data, *args, **kwargs):
            self._set_allowed_params(data)
            validated_data = self._get_validated_data(data)
            return func(paren_class, validated_data, *args, **kwargs)
        return decorated


class OnlyAllowedParamsUpdate(OnlyAllowedParams):
    def __call__(self, func, *args, **kwargs):
        @functools.wraps(func)
        def decorated(paren_class, instance, data, *args, **kwargs):
            self._set_allowed_params(data)
            validated_data = self._get_validated_data(data)
            return func(paren_class, instance, validated_data, *args, **kwargs)
        return decorated














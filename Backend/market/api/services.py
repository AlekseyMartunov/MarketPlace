from copy import deepcopy
import functools

from rest_framework import serializers


class OnlyAllowedParams:
    """
    Класс для проверки данных jsonField
    """
    def __init__(self, key, indx):
        self._key = key
        self._allowed_params = None
        self._index_for_data = indx

    def __call__(self, func):
        @functools.wraps(func)
        def decorated(*args, **kwargs):
            args = list(args)
            args[self._index_for_data] = self._get_validated_data(args[self._index_for_data])
            result = func(*args, **kwargs)
            return result
        return decorated

    def _get_validated_data(self, old_data: dict) -> dict:
        self._allowed_params = old_data.get('category').allowed_params[self._key]
        date = deepcopy(old_data)
        validated = self._validate_data(date[self._key])
        date.pop(self._key)
        date.setdefault(self._key, validated)
        return date

    def _validate_data(self, data: dict) -> dict:
        val_keys = self._validate_keys(data)
        self._validate_values(val_keys)
        return val_keys

    def _validate_keys(self, data: dict) -> dict:
        keys = self._allowed_params.keys()
        val_data = {key: value for key, value in data.items() if key in keys}

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















from copy import deepcopy
import functools

from rest_framework import serializers


class OnlyAllowedParams:
    """
     Базовый класс для проверки данных jsonField
    """
    def __init__(self, validate_field: str):
        self._key = validate_field
        self._allowed_params = None
        self._errors = {}
        self._is_valid = True

    def __call__(self, *args, **kwargs):
        raise NotImplementedError()

    def _get_validated_data(self, not_valid_data: dict) -> dict:
        date = deepcopy(not_valid_data)
        validated = self._validate_data(date[self._key])
        date.pop(self._key)
        date.setdefault(self._key, validated)
        return date

    def _validate_data(self, data: dict) -> dict:
        self._errors = {}

        val_keys = self._validate_keys(data)
        self._validate_values(val_keys)
        if not self._is_valid:
            self._raise_exception()
        return val_keys

    def _validate_keys(self, data: dict) -> dict:
        val_keys = {key: value for key, value in data.items() if key in self._allowed_params.keys()}

        if len(val_keys) < len(self._allowed_params):
            empty_keys = set(self._allowed_params.keys()).difference(val_keys.keys())
            self._is_valid = False
            self._errors.update({
                key: ["missing key", ] for key in empty_keys
            })
        return val_keys

    def _validate_values(self, data: dict):
        types_dict = {
            'number': int,
            'string': str,
            'bool': bool,
        }

        # data -> {price: 1000, ...}   self._allowed_params -> {price: "number", ...}

        for key, value in data.items():
            type_validator = self._allowed_params.get(key)
            if types_dict[type_validator] != type(data[key]):
                self._is_valid = False
                self._errors.update({
                    key: [f"This field should be {type_validator}", ]
                })

    def _set_allowed_params(self, data: dict):
        self._allowed_params = data.get('category').allowed_params

    def _raise_exception(self):
        self._is_valid = True
        raise serializers.ValidationError(self._errors)


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














import functools
from rest_framework import serializers
from objects.models import Category

# allowed params {
# "mass": "number",
# "color": {
#       "choice": [red, blue, green, black],
#       "many": False}
# }


class NumberValidator:
    def is_valid(self, value: int|float) -> bool:
        return type(value) in (int, float)


class ChoseValidator:
    def __init__(self, params: dict):
        self.choice = params["choice"]
        self.many = params["many"]

    def is_valid(self, value: list) -> bool:
        # if not isinstance(value, list) or value:
        #     return False
        if not self.many and len(value) > 1:
            return False
        for element in value:
            if element not in self.choice:
                return False

        return True



class OnlyAllowedParams:
    """
    Базовый класс для проверки данных jsonField
    """

    def __init__(self):
        self.allowed_params = {}
        self.errors = {}

    def __call__(self, func, *args, **kwargs):
        @functools.wraps(func)
        def decorated(paren_class, validated_data):
            print(validated_data)
            self._set_allowed_params(validated_data['category'])
            new_data = self._validate_data(validated_data["params"])
            validated_data["params"] = new_data
            return func(paren_class, validated_data)

        return decorated

    def _validate_data(self, data):
        data = self._validate_keys(data)
        data = self.validate_values(data)
        if self.errors:
            self._raise_exception()
        return data

    def _validate_keys(self, data):
        val_data = {key: value for key, value in data.items() if key in self.allowed_params.keys()}

        if len(self.allowed_params) > len(val_data):
            lost_keys = set(self.allowed_params.keys()).difference(val_data.keys())
            self.errors.update({
                key: "missing key" for key in lost_keys
            })

        return val_data

    def validate_values(self, data):
        for key in data.keys():
            field = self.allowed_params[key]
            validator = self._get_validator_for_field(field)
            if not validator.is_valid(data[key]):
                self.errors.update({key: "Wrong type"})
        return data

    def _set_allowed_params(self, category):
        self.allowed_params = category.allowed_params

    def _get_validator_for_field(self, field):
        if isinstance(field, str):
            return NumberValidator()
        if isinstance(field, dict):
            return ChoseValidator(field)

    def _raise_exception(self):
        err = self.errors
        self.errors = {}
        raise serializers.ValidationError(err)

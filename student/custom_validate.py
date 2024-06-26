from django.core.validators import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_no_digit_and_special_characters(value):
    if any(char.isdigit() or not char.isalpha() for char in value):
        # print('This field should not contain digits or special characters.')
        raise ValidationError(
            _('This field should not contain digits or special characters.')
        )

def validate_mobile_number_length(value):
    if len(value) != 10 or not value.isdigit():
        # print('Mobile number must be exactly 10 digits long.')
        raise ValidationError(
            _('Mobile number must be exactly 10 digits long.')
        )
from django.db import models
from django.core.validators import EmailValidator, MaxLengthValidator, MinLengthValidator
from student.custom_validate import validate_no_digit_and_special_characters, validate_mobile_number_length

class StudentInfo(models.Model):
    student_id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=70, validators=[validate_no_digit_and_special_characters])
    last_name = models.CharField(max_length=70, validators=[validate_no_digit_and_special_characters])
    mobile_number = models.CharField(max_length=10, unique=True, validators=[validate_mobile_number_length])
    email = models.EmailField(max_length=100, unique=True, validators=[EmailValidator(message='Enter a valid email address.')])
    address = models.TextField(max_length=500, validators=[
        MinLengthValidator(3, message='Address must be at least 3 characters long.'),
        MaxLengthValidator(500, message='Address cannot exceed 500 characters.')
    ])

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self):
        return f"{self.first_name}"

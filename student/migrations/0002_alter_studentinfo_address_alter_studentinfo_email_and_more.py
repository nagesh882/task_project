# Generated by Django 5.0.6 on 2024-06-25 19:09

import django.core.validators
import student.custom_validate
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinfo',
            name='address',
            field=models.TextField(max_length=500, validators=[django.core.validators.MinLengthValidator(3, message='Address must be at least 3 characters long.'), django.core.validators.MaxLengthValidator(500, message='Address cannot exceed 500 characters.')]),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='email',
            field=models.EmailField(max_length=100, unique=True, validators=[django.core.validators.EmailValidator(message='Enter a valid email address.')]),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='first_name',
            field=models.CharField(max_length=70, validators=[student.custom_validate.validate_no_digit_and_special_characters]),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='last_name',
            field=models.CharField(max_length=70, validators=[student.custom_validate.validate_no_digit_and_special_characters]),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='mobile_number',
            field=models.CharField(max_length=10, unique=True, validators=[student.custom_validate.validate_mobile_number_length]),
        ),
    ]
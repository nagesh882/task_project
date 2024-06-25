from typing import Any
from django import forms
from student.models import StudentInfo
from django.core.validators import validate_email



class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentInfo
        fields = ['first_name','last_name','mobile_number','email','address']
        # fields = "__all__"
        widgets = {
            'first_name':forms.TextInput(attrs={'placeholder':'Enter first name', 'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'placeholder':'Enter last name', 'class':'form-control'}),
            'mobile_number':forms.TextInput(attrs={'placeholder':'Enter mobile number', 'class':'form-control'}),
            'email':forms.EmailInput(attrs={'placeholder':'Enter email', 'class':'form-control'}),
            'address':forms.Textarea(attrs={'placeholder':'Enter address', 'class':'form-control', 'rows':2}),
        }

    # Custom validation for each fields 
    def clean(self):
        cleaned_data = super().clean()
        fisrt_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        email = cleaned_data.get('email')
        mobile_number = cleaned_data.get('mobile_number')
        address = cleaned_data.get('address')

        if any(char.isdigit() or not char.isalpha() for char in fisrt_name):
            raise forms.ValidationError('This field should not contain digits or special characters.')
        
        if any(char.isdigit() or not char.isalpha() for char in last_name):
            raise forms.ValidationError('This field should not contain digits or special characters.')
        
        if validate_email(email):
            raise forms.ValidationError('Enter a valid email address.')
        
        if len(mobile_number) != 10 or not mobile_number.isdigit():
            raise forms.ValidationError('Mobile number must be exactly 10 digits long.')

        if len(address) < 3 or len(address) > 500:
            raise forms.ValidationError('Address must be at least 3 and less than 500 characters long.')







# class StudentEditForm(forms.ModelForm):
#     class Meta:
#         model = StudentInfo
#         # fields = ['first_name','last_name','mobile_number','email','address']
#         fields = "__all__"
#         widgets = {
#             'first_name':forms.TextInput(attrs={'placeholder':'Enter first name', 'class':'form-control'}),
#             'last_name':forms.TextInput(attrs={'placeholder':'Enter last name', 'class':'form-control'}),
#             'mobile_number':forms.TextInput(attrs={'placeholder':'Enter mobile number', 'class':'form-control'}),
#             'email':forms.EmailInput(attrs={'placeholder':'Enter email', 'class':'form-control'}),
#             'address':forms.Textarea(attrs={'placeholder':'Enter address', 'class':'form-control', 'rows':2}),
#         }

#     def clean(self):
#         cleaned_data = super().clean()
#         fisrt_name = cleaned_data.get('first_name')
#         last_name = cleaned_data.get('last_name')
#         email = cleaned_data.get('email')
#         mobile_number = cleaned_data.get('mobile_number')
#         address = cleaned_data.get('address')

#         if any(char.isdigit() or not char.isalpha() for char in fisrt_name):
#             raise forms.ValidationError('This field should not contain digits or special characters.')
        
#         if any(char.isdigit() or not char.isalpha() for char in last_name):
#             raise forms.ValidationError('This field should not contain digits or special characters.')
        
#         if not validate_email(email):
#             raise forms.ValidationError('Enter a valid email address.')
        
#         if len(mobile_number) != 10 or not mobile_number.isdigit():
#             raise forms.ValidationError('Mobile number must be exactly 10 digits long.')

#         if len(address) < 3 or len(address) > 500:
#             raise forms.ValidationError('Address must be at least 3 and less than 500 characters long.')
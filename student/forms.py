from django import forms
from student.models import StudentInfo



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



class StudentEditForm(forms.ModelForm):
    class Meta:
        model = StudentInfo
        # fields = ['first_name','last_name','mobile_number','email','address']
        fields = "__all__"
        widgets = {
            'first_name':forms.TextInput(attrs={'placeholder':'Enter first name', 'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'placeholder':'Enter last name', 'class':'form-control'}),
            'mobile_number':forms.TextInput(attrs={'placeholder':'Enter mobile number', 'class':'form-control'}),
            'email':forms.EmailInput(attrs={'placeholder':'Enter email', 'class':'form-control'}),
            'address':forms.Textarea(attrs={'placeholder':'Enter address', 'class':'form-control', 'rows':2}),
        }

from django import forms
from .models import User
class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['fname', 'mname' , 'lname', 'age', 'gender', 'address', 'email', 'mobno', 'alemail', 'almobno', 'fathername', 'mothername', 'insname']
        widgets = {
            'fname': forms.TextInput(attrs={'class': 'form-control'}),
            'mname': forms.TextInput(attrs={'class': 'form-control'}),
            'lname': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'mobno': forms.TextInput(attrs={'class': 'form-control'}),
            'alemail': forms.EmailInput(attrs={'class': 'form-control'}),
            'almobno': forms.TextInput(attrs={'class': 'form-control'}),
            'fathername': forms.TextInput(attrs={'class': 'form-control'}),
            'mothername': forms.TextInput(attrs={'class': 'form-control'}),
            'insname': forms.TextInput(attrs={'class': 'form-control'}),

        }

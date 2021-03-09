from django import forms
from APP1.models import Student
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

class signupStudent(forms.Form):
    Email_s = forms.EmailField( label ='Email:')
    degree_of_education_p = forms.FileField( label='Degree_Of_Education:')
    name_p = forms.CharField( label ='Professor Name:',max_length = 50 )
    uni = forms.CharField( label ='University',max_length = 50 )
    name_s = forms.CharField( label ='Student Name',max_length = 50 )
    family_s = forms.CharField( label ='Student Family',max_length = 50 )
    age_s = forms.IntegerField( label='Age')
    number_of_student = forms.IntegerField(label='Student Number')
    password_s = forms.CharField(widget=forms.PasswordInput)
    widgets = {
        'password_s': forms.PasswordInput(),
        }
    username_s = forms.CharField( label ='Username',max_length = 50 )
    


class loginform(forms.Form):
    username= forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    widgets = {
        'password': forms.PasswordInput(),
    }
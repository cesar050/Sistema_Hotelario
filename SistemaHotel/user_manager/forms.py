from django import forms

class UserManagerForm(forms.Form):
    username = forms.CharField(label='Username', max_length=150)
    first_name = forms.CharField(label='First Name', max_length=50)
    last_name = forms.CharField(label='Last Name', max_length=50)
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

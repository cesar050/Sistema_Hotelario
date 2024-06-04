from django import forms

class HotelManagerForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=50)
    last_name = forms.CharField(label='Last Name', max_length=50)
    email = forms.EmailField(label='Email')
    phone_number = forms.CharField(label='Phone Number', max_length=15)
    hotel = forms.CharField(label='Hotel', max_length=100)

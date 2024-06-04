from django import forms

class AdminHotelForm(forms.Form):
    name = forms.CharField(label='Hotel Name', max_length=100)
    address = forms.CharField(label='Address', max_length=255)
    phone_number = forms.CharField(label='Phone Number', max_length=15)
    email = forms.EmailField(label='Email')

from django import forms

class ReservationManagerForm(forms.Form):
    guest_name = forms.CharField(label='Guest Name', max_length=100)
    room_type = forms.ChoiceField(label='Room Type', choices=[('Single', 'Single'), ('Double', 'Double'), ('Suite', 'Suite')])
    check_in_date = forms.DateField(label='Check-In Date')
    check_out_date = forms.DateField(label='Check-Out Date')
    special_requests = forms.CharField(label='Special Requests', widget=forms.Textarea, required=False)

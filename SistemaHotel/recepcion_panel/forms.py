from django import forms

class ReceptionPanelForm(forms.Form):
    guest_name = forms.CharField(label='Guest Name', max_length=100)
    check_in_date = forms.DateField(label='Check-In Date')
    check_out_date = forms.DateField(label='Check-Out Date')
    room_number = forms.CharField(label='Room Number', max_length=10)
    payment_status = forms.ChoiceField(label='Payment Status', choices=[('Paid', 'Paid'), ('Unpaid', 'Unpaid')])

from django import forms

class CorrForm(forms.Form):
    # course      =forms.Charfiel 
    # enroll_year =
    # section     =
    favorite_fruit= forms.CharField(label='What is your favorite fruit?', widget=forms.Select(choices=('A', 'B', 'C')))

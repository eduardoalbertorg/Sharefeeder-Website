from django import forms
from django.core.exceptions import ValidationError


class FeederForm(forms.Form):
    feederId = forms.IntegerField()

    def clean_feederId(self):
        data = self.cleaned_data['feederId']
        # Check if id is positive and bigger than 1
        if data < 1:
            raise ValidationError('Not a valid Feeder ID')
        return data
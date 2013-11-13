from django import forms
from models import Incident


class IncidentForm(forms.ModelForm):

    class Meta:
        model = Incident
        fields = ('title', 'description', 'company', 'requestor')
        widgets = {
            'company': forms.HiddenInput(),
            'requestor': forms.HiddenInput()
        }

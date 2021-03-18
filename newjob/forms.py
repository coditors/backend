
from django import forms
from .models import Newjob

class NewjobForm(forms.ModelForm):

    class Meta:
        model = Newjob
        fields = ['title', 'type', 'background', 'price', 'image']
from .models import Upload
from django import forms

class updateforms(forms.ModelForm):
    class Meta:
        model=Upload
        fields=['file','user_id']
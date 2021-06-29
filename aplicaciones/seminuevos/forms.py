from django import forms
from .models import Seminuevo

class SeminuevoForm(forms.ModelForm):
    class Meta:
        model = Seminuevo
        fields = '__all__'
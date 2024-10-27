from django import forms
from pages.models import CurrencySign,Tags

class CurrencyForm(forms.Form):
    cur_id = forms.CharField()
    cur_name = forms.CharField()
    cur_sign = forms.ModelChoiceField(CurrencySign.objects.all())
    cur_tag = forms.ModelMultipleChoiceField(Tags.objects.all())

class CurrecnySignForm(forms.Form):
    cur_sign = forms.CharField()
    sign = forms.CharField()
        

from django import forms

class AddForm(forms.Form):
    yourmobile = forms.CharField(max_length=100)
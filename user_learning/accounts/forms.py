from django import forms
from accounts.models import Classes, Table

class ClassForm(forms.ModelForm):
    class Meta:
        model = Classes
        fields = ('school','capasity')

class TableForm(forms.ModelForm):
    class Meta:
        model = Table
        exclude = ('user')

from dataclasses import fields
from django import forms
from django.core.exceptions import ValidationError

from .models import Project, Address

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('name','po','address','permitNumber','status', 'bidNumber',
                    'contractCompleteDate','projectedStartDate')

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('street','unit','city','state','zip')
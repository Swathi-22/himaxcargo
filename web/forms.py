from django import forms
from django.forms.widgets import EmailInput
from django.forms.widgets import FileInput
from django.forms.widgets import Select
from django.forms.widgets import Textarea
from django.forms.widgets import TextInput
from .models import CargoRequest


class CargoRequestForm(forms.ModelForm):
    class Meta:
        model = CargoRequest
        fields = "__all__"
        widgets = {
            "services": Select(attrs={"class": "custom-select",}),
            "length": TextInput(attrs={"placeholder":"Length cm"}),
            "width": Select(attrs={"placeholder":"Width cm"}),
            "from_country": Select(attrs={"class": "custom-select"}),
            "to_country": TextInput(attrs={"class": "custom-select"}),
            "weight": TextInput(attrs={"class": "custom-select"}),
            "phone": TextInput(attrs={"class": "cta-email"}),
        }
from django import forms
from django.forms.widgets import EmailInput
from django.forms.widgets import FileInput
from django.forms.widgets import Select
from django.forms.widgets import Textarea
from django.forms.widgets import TextInput
from .models import CargoRequest
from .models import Contact



class CargoRequestForm(forms.ModelForm):
    class Meta:
        model = CargoRequest
        fields = "__all__"
        widgets = {
            "services": Select(attrs={"class": "form-control form-color"}),
            "length": TextInput(attrs={"class": "form-control form-color"}),
            "width": TextInput(attrs={"class": "form-control form-color"}),
            "from_country": Select(attrs={"class": "form-control form-color"}),
            "to_country": Select(attrs={"class": "form-control form-color"}),
            "weight": Select(attrs={"class": "form-control form-color"}),
            "phone": TextInput(attrs={"class": "form-control form-color"}),
        }



class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields='__all__'
        widgets={
            'name':TextInput(attrs={'placeholder':"Your Name",}),
            'email':EmailInput(attrs={'placeholder':"Your Email",}),
            'phone':TextInput(attrs={'placeholder':"Your Phone",}),
            'subject':TextInput(attrs={'placeholder':"Subject",}),
            'message':Textarea(attrs={'placeholder':"Message",'rows':"6"}),
         }
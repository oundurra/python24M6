from django import forms
from .models import Contact

class ContactFormModel(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['customer_email', 'customer_name', 'message']

class ContactForm(forms.Form):
    customer_email = forms.EmailField(label = 'Correo')
    customer_name = forms.CharField(label = 'Nombre', max_length=64)
    message = forms.CharField(label = 'Message')
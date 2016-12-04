from django import forms
from django.core.exceptions import ValidationError

from contacts.models import Contact


class ContactForm(forms.ModelForm):

    mandatory_bro = forms.EmailField(
        label="Confirm email",
        required=True,
    )
    class Meta:
        model = Contact
        fields = '__all__'

    def __init__(self, *args, **kwargs):

        if kwargs.get('instance'):
            email = kwargs['instance'].Faculty_email
            kwargs.setdefault('initial', {})['Confirm_email'] = email

        return super(ContactForm, self).__init__(*args, **kwargs)
    

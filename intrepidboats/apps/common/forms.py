from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.utils.translation import ugettext as _
from nocaptcha_recaptcha.fields import NoReCaptchaField

from .models import NewsletterSubscriber


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscriber
        fields = ('first_name', 'last_name', 'email')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'input', 'placeholder': _('First name')}),
            'last_name': forms.TextInput(attrs={'class': 'input', 'placeholder': _('Last name')}),
            'email': forms.EmailInput(attrs={'class': 'input', 'placeholder': _('Email address')}),
        }


class UserRegistrationForm(ModelForm):
    password_repeat = forms.CharField(required=True, widget=forms.PasswordInput())
    email_repeat = forms.EmailField(required=True)
    phone = forms.CharField(required=False)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    fan = forms.BooleanField(required=False)
    intrepid_model = forms.CharField(required=False)
    intrepid_year = forms.CharField(required=False)
    intrepid_hull_id = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        is_mobile = kwargs.pop('request').flavour == 'mobile'
        super().__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = ('email', 'password', 'username', 'first_name', 'last_name',)
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean_password(self):
        if self.data['password'] != self.data['password_repeat']:
            self.add_error('password', "Passwords don't match")
        return self.data['password']

    def clean(self):
        if self.data['email'] != self.data['email_repeat']:
            self.add_error('email', "Emails don't match")
        return super(UserRegistrationForm, self).clean()

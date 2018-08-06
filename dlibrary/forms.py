from django import forms
from django.urls.base import reverse_lazy
from captcha.fields import CaptchaField

from dlibrary.models import Suser


class SuserForm(forms.ModelForm):
    name = forms.CharField()
    city = forms.CharField()
    state = forms.CharField()
    phone = forms.CharField()
    myimg = forms.ImageField()
    captcha = CaptchaField()
    class Meta:
        model = Suser
        fields = ['name', 'city', 'state','phone']
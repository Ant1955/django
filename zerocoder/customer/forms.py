from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

from .models import Account
class RegistrationForm(UserCreationForm):
    username = forms.CharField(required=True, label="Логин")
    email = forms.CharField(required=True)
    f_name = forms.CharField(required=True, label="Имя")
    l_name = forms.CharField(required=True, label="Фамилия")
    phone_number = forms.RegexField(regex=r'^\+?1?\d{9,12}$', label="Телефон", error_messages={
        'invalid': 'Введите правильно номер телефона!'
    }, required=True)

    class Meta:
        model = Account
        fields = ("username", "email", "f_name", "l_name", "phone_number", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)


class AccountAuthenticationForm(forms.ModelForm):
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ("email", "password")

    def __init__(self, *args, **kwargs):
        super(AccountAuthenticationForm, self).__init__(*args, **kwargs)

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data.get("email")
            password = self.cleaned_data.get("password")
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Email или пароль введены неверно!")

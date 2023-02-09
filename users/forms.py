from .models import UserProfile
from django import forms
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField, CaptchaTextInput, CaptchaAnswerInput


class CustomCaptchaTextInput(CaptchaTextInput):
    template_name = 'custom_field.html'


class RegisterForm(forms.ModelForm):
    captcha = CaptchaField(required=False,
                           widget=CustomCaptchaTextInput(attrs={
                                                                'class': 'verifyCode input',
                                                                }),
                           error_messages={'invalid': 'Неправильный код проверки.'})

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'maxlength': '128',
        'required': 'required',
        'class': 'input'
    }))
    repeat_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'maxlength': '128',
        'required': 'required',
        'class': 'input'
    }))

    class Meta:
        model = UserProfile
        fields = ['user_login', 'socials']

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['user_login'].widget.attrs \
            .update({
            'class': 'input',
            'maxlength': '20',
            'required': 'required'
        })
        self.fields['socials'].widget.attrs \
            .update({
            'class': 'input',
            'maxlength': '128',
            'type': 'text'
        })
        self.fields['socials'].required = False

    def clean_repeat_password(self):
        password = self.cleaned_data.get('password')
        repeat_password = self.cleaned_data.get('repeat_password')

        if password != repeat_password:
            raise ValidationError('Пароль должен быть повторен в точности.')
        return repeat_password


class LoginForm(forms.Form):
    captcha = CaptchaField(required=False,
                           widget=CustomCaptchaTextInput(attrs={
                               'class': 'verifyCode input',
                           }),
                           error_messages={'invalid': 'Неправильный код проверки.'})

    login = forms.CharField(max_length=50, required=False, label='Логин',
                            widget=forms.TextInput(attrs={'required': 'required',
                                                          'class': 'input'}))

    password = forms.CharField(max_length=150, required=False, widget=forms.PasswordInput(attrs={'required': 'required',
                                                                                                 'class': 'input'}))




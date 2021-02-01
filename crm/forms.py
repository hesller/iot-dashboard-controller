from django.contrib.auth import authenticate
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext, gettext_lazy as _

from crm import models


class UserAuthenticationForm(forms.Form):
    """
        Base class for authenticating users. Extend this to get a form that accepts
        email/password logins.
    """

    email = forms.CharField(max_length=255, label='Email', required=True)
    password = forms.CharField(max_length=255, label='Password', required=True, widget=forms.PasswordInput())

    error_messages = {
        'invalid_login': _(
            "Por favor verifique se o email: %(email)s e senha, estão corretos."
        ),
        'inactive': _("Esta conta está inativa."),
    }

    def __init__(self, request=None, *args, **kwargs):
        """
        The 'request' parameter is set for custom auth use by subclasses.
        The form data comes in via the standard 'data' kwarg.
        """
        self.request = request
        self.user_cache = None
        super().__init__(*args, **kwargs)


    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        print('inside clean method')

        if email is not None and password:
            self.user_cache = authenticate(self.request, username=email, password=password)
            if self.user_cache is None:
                self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

    def clean_password(self):
        password = self.cleaned_data.get('password')

        if len(password) < 8:
            raise ValidationError('Senha muito curta! Lembre-se que a senha deve conter no mínimo 8 caracteres.')
        return password

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if validate_email(email):
            raise ValidationError('Email inválido')
        return email

    def confirm_login_allowed(self, user):
        """
        Controls whether the given User may log in. This is a policy setting,
        independent of end-user authentication. This default behavior is to
        allow login by active users, and reject login by inactive users.

        If the given user cannot log in, this method should raise a
        ``ValidationError``.

        If the given user may log in, this method should return None.
        """
        if not user.is_active:
            raise ValidationError(
                self.error_messages['inactive'],
                code='inactive',
            )

    def get_invalid_login_error(self):
        raise ValidationError(
            self.error_messages['invalid_login'],
            code='invalid_login',
            params={'email': self.cleaned_data.get('email')},
        )

    def get_user(self):
        return self.user_cache


class EnvironmentCreateForm(forms.ModelForm):

    class Meta:
        model = models.Environment
        fields = ['name', 'local', 't_t']


class AirConditioningCreateForm(forms.ModelForm):
    class Meta:
        model = models.AirConditioning
        exclude = ['environment']


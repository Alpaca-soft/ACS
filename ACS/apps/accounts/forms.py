from django import forms
from django.contrib.auth import (authenticate, get_user_model, login, logout,)

User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField(label="Имя пользователя")
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль")

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Неверно введены пользовательские данные.')
            if not user.check_password(password):
                raise forms.ValidationError("Неверный пароль.")
            if not user.is_active:
                raise forms.ValidationError("Данная учётная запись заблокирована.")
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label='Введите е-мейл')
    email2 = forms.EmailField(label='Повторите е-мейл')
    password = forms.CharField(label='Ведите пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'email2',
            'password',
            'password2',
        ]

    def clean_email2(self):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            raise forms.ValidationError("Несовпадает почта.")
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("Введённая почта уже используется.")
        return email

    def clean_pass2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError("Пароли не совпадают.")
        return password


class UserEditForm(forms.ModelForm):
    template_name = '/something/else'

    class Meta:
        model = User
        fields = [
            'email',
            'first_name',
            'last_name',
            'password'
        ]

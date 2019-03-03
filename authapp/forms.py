import hashlib
import random
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from authapp.models import CustomUser, CustomUserProfile


class LoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'age', 'password1', 'password2', 'email', 'first_name', 'avatar')

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

#    проверка на 18 лет
#     def clean_age(self):
#         data = self.cleaned_data['age']
#         if data < 18:
#             raise forms.ValidationError('Недопустимый возраст. Только 18+')
#         return data

#    переопределяем метод save для формы регистрации пользователя
    def save(self):
        user = super(RegisterForm, self).save()

        user.is_active = False
        salt = hashlib.sha1(str(random.random()).encode('utf8')).hexdigest()[:6]
        user.activation_key = hashlib.sha1((user.email + salt).encode('utf8')).hexdigest()
        user.save()

        return user


class UpdateForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'age', 'password', 'email', 'first_name', 'avatar')

    def __init__(self, *args, **kwargs):
        super(UpdateForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

            if field_name == 'password':
                field.widget = forms.HiddenInput()


class CustomUserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUserProfile
        fields = ('tagline', 'aboutMe', 'gender')

    def __init__(self, *args, **kwargs):
        super(CustomUserProfileUpdateForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

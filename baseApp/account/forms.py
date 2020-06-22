from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    password1 = forms.CharField(label='Pessword', max_length=100)
    password2 = forms.CharField(label='Confirm password', max_length=100)

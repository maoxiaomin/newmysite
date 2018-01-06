from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=50, required=True)
    password = forms.CharField(label='密码', max_length=128, required=True, widget=forms.PasswordInput)
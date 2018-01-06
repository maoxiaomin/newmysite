from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth import authenticate, login
from . import forms

# Create your views here.
class LoginView(View):
    def get(self, request):
        login_form = forms.LoginForm()
        return render(request, 'login.html', locals())

    def post(self, request):
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            # 和数据库比对
            user = authenticate(username=username, password=password)
            if user:
                # 回填user内容
                login(request, user)
                return render(request, 'index.html')
            else:
                message =  '用户名或密码错误'
                return render(request, 'login.html', locals())

        return render(request, 'login.html', locals())

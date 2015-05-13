#coding=utf8
from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    username=forms.CharField(max_length=30,label="用户名")
    passwd1=forms.CharField(min_length=6,widget=forms.PasswordInput,label="密码")
    passwd2=forms.CharField(min_length=6,widget=forms.PasswordInput,label="密码")
    email=forms.EmailField(required=False,label="邮箱(可选)")

    def clean(self):
        cleand_data=super(RegisterForm,self).clean()
        passwd1=cleand_data.get("passwd1")
        passwd2=cleand_data.get("passwd2")

        if passwd1 and passwd2 and passwd1!=passwd2:
            self._errors["passwd2"]=self.error_class(["2次密码不一致"])
        return cleand_data

class LoginForm(forms.Form):
    username=forms.CharField(max_length=30,label="用户名")
    password=forms.CharField(widget=forms.PasswordInput,label="密码")
        

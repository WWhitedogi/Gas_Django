from django.shortcuts import render, HttpResponse, redirect
from django import forms
from io import BytesIO
from app01 import models
from app01.utils.bootstrap import BootStrapForm
from app01.utils.encrypt import md5
from app01.utils.code import check_code
from io import BytesIO

import hashlib

class LoginForm(BootStrapForm):
    username = forms.CharField(
        label="username",
        widget=forms.TextInput,
        required=True
    )
    password = forms.CharField(
        label="password",
        widget=forms.PasswordInput(render_value=True),
        required=True
    )
    code = forms.CharField(
        label="enter the character",
        widget=forms.TextInput,
        required=True
    )

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        return md5(pwd)


def login(request):
    """ 登录 """
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    form = LoginForm(data=request.POST)
    if form.is_valid():
        # 验证成功，获取到的用户名和密码
        # {'username': 'wupeiqi', 'password': '123',"code":123}
        # {'username': 'wupeiqi', 'password': '5e5c3bad7eb35cba3638e145c830c35f',"code":xxx}
        #验证码校验

        #用户输入的
        user_input_code=form.cleaned_data.pop('code')
        #图片上的
        code=request.session.get('image_code',"")
        if code != user_input_code.upper():
            form.add_error("code","验证码错误")
            return render(request,'login.html',{'form':form})


        # 去数据库校验用户名和密码是否正确，获取用户对象、None
        # admin_object = models.Admin.objects.filter(username=xxx, password=xxx).first()
        admin_object = models.Admin.objects.filter(**form.cleaned_data).first()
        if not admin_object:
            form.add_error("password", "用户名或密码错误")
            return render(request, 'login.html', {'form': form})

        # 用户名和密码正确
        # 网站生成随机字符串; 写到用户浏览器的cookie中；在写入到session中；
        request.session["info"] = {'id': admin_object.id, 'name': admin_object.username}
        #用户信息保存七天，免登录
        request.session.set_expiry(60*60*24*7)

        return redirect("/admin/list/")

    return render(request, 'login.html', {'form': form})

def image_code(request):

    """调用pillow函数"""
    img,code_string=check_code()
    print(code_string)
    #写入到自己的session中（以便于获取验证码校验）
    request.session['image_code']=code_string
    #session设置60秒超时
    request.session.set_expiry(60)

    stream=BytesIO()
    img.save(stream,'png')

    return HttpResponse(stream.getvalue())

def logout(request):
    """ 注销 """

    request.session.clear()

    return redirect('/login/')

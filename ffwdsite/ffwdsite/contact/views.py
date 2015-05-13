#coding=utf8
from django.shortcuts import render_to_response,render
from django.template import RequestContext
from ffwdsite.contact.forms import RegisterForm,LoginForm
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from mydb.models import Blog_user,Blog_comment,Blog_essay
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import auth

class RegisterView(FormView):
    #template_name='test.html'
    form_class=RegisterForm
    #success_url=request.path
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            try:
                newuser=User.objects.create(
                    username=form.cleaned_data['username'],
                    email=form.cleaned_data['email'],
                    )
                newuser.set_password(form.cleaned_data['passwd1'])
                newuser.save()
                wuser=Blog_user.objects.create(user_id=User.objects.get(username=form.cleaned_data['username']).id)
                wuser.save()
            except:
                return HttpResponse('sorry，用户已存在')
            else:
                loginuser=form.cleaned_data['username']
                passwd=form.cleaned_data['passwd1']
                user=auth.authenticate(username=loginuser,password=passwd)
                auth.login(request,user)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
        #return render(request,self.template_name,{'form':form})

class LoginView(FormView):
    form_class=LoginForm
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            loginuser=form.cleaned_data['username']
            passwd=form.cleaned_data['password']
            user=auth.authenticate(username=loginuser,password=passwd)
            if user is not None and user.is_active:
                auth.login(request,user)
                return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
            else:
                return HttpResponse('sorry，登录失败')
        return HttpResponse('sorry，表单提交失败')
        
def Comment(request):
    if request.method=='POST':
        if request.POST.get('message','').strip()!='':
            comment=request.POST['message']
            username=request.POST['username']
            essayid=request.POST['essayid']
            userid=User.objects.get(username=username).blog_user.id
            #if request.POST['comtype']!=None:
            try:
                new_comment=Blog_comment.objects.create(comment=comment,blog_essay_id=essayid,blog_user_id=userid,comtype=request.POST['comtype'])
            except:
                new_comment=Blog_comment.objects.create(comment=comment,blog_essay_id=essayid,blog_user_id=userid)
            new_comment.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))

#coding=utf8
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template.loader import get_template
from django.shortcuts import render_to_response
from mydb.models import Blog_user,Blog_essay,Blog_tag,Blog_inspire,Blog_comment
from django.template import RequestContext
from django.db.models import Q
from redis import Redis
from ffwdsite.contact.forms import RegisterForm,LoginForm
import time

#views
def Test(request):
    request.session['foo']='213'
    del request.session['foo']
    refer=request.META.get('HTTP_REFERER','No REFERER')
#-----------
    comments=Blog_comment.objects.filter(Q(blog_essay_id=8)&Q(comtype=0)).order_by('comtime')
    com_lzllist=[]
    for i in comments:
        lzllist=Blog_comment.objects.filter(comtype=i.id).order_by('comtime')
        com_lzllist.append((i,lzllist))
#-------------
    response= render_to_response('test.html',{'refer':refer,'testcomments':com_lzllist,'form_login':LoginForm,'form':RegisterForm,'cookies':request.COOKIES},RequestContext(request,))
    response.set_cookie("fav","ccccccc")
    return response
    #return render_to_response('test.html',RequestContext(request,{'cookies':request.COOKIES},processors=[costom]))
#-------------------------------------------------------------------------------------
def Index(request):
    return render_to_response('index.html',RequestContext(request))
#----------------------- cp content0.html select0.html ,del left ------------
def content_if(request,titles_id,t_id,html=('select.html','content.html')):
    if t_id=='999':
        return '',html[0]
    else:
        essay_id=Blog_essay.objects.get(id=t_id)
        #online 
        if 'HTTP_X_REAL_IP' in request.META:
            ip=request.META['HTTP_X_REAL_IP']
        else:
            ip=request.META['REMOTE_ADDR']
        r11=Redis(host='localhost',port=6379,db=11,password='ffwd')
        #ip不在redis对应的t_id命名集合key中(是不是今天第一次访问文章)
        if ip not in r11.smembers('essay'+t_id):
            #redis: 新增或追加一个essayid的set key，并存入一个ip，ip重复则抵消
            r11.sadd('essay'+t_id,ip)
            #过期时间 现在离今天23点59分59秒还有多少秒，为过期时间
            extime=time.mktime(time.strptime(time.strftime('%Y%m%d')+' 23:59:59','%Y%m%d %X'))-time.time()
            r11.expire('essay'+t_id,int(extime))
            #t_id文章浏览量+1，保存到mysql
            essay_id.page_view+=1
            essay_id.save()
        return essay_id,html[1]
def Content(request,type,t_id):
    #学习
    if type=="0":
        titles_id=Blog_essay.objects.filter(~Q(tag_id=4)&~Q(tag_id=3)).order_by('-createtime')
        title_top='学习笔记'
        content,go_html=content_if(request,titles_id,t_id)
    #工具
    elif type=="1":
        titles_id=Blog_essay.objects.filter(tag=4).order_by('-createtime')
        title_top='工具'
        content,go_html=content_if(request,titles_id,t_id)
    #生活
    elif type=="2":
        titles_id=Blog_essay.objects.filter(tag=3).order_by('-createtime')
        title_top='生活'
        content,go_html=content_if(request,titles_id,t_id)
    #标签
    elif type=="3":
        titles_id=[]
        for tag in Blog_tag.objects.all():
            titles_id.append((tag,Blog_essay.objects.filter(tag_id=tag.id)))
        title_top='标签'
        content,go_html=content_if(request,titles_id,t_id)
    #监控
    elif type=="4":
        return HttpResponseRedirect('http://www.feifeiwd.com:8100')
        #return render_to_response('creating.html',RequestContext(request))
    #论坛
    elif type=="5":
        return render_to_response('creating.html',RequestContext(request))
    #关于
    elif type=="6" and t_id=='999':
        return render_to_response('about.html',RequestContext(request))
    else:
        raise Http404
    #评论系统
    comments=Blog_comment.objects.filter(Q(blog_essay_id=t_id)&Q(comtype=0)).order_by('comtime')
    com_lzllist=[]
    for i in comments:
        lzllist=Blog_comment.objects.filter(comtype=i.id).order_by('comtime')
        com_lzllist.append((i,lzllist))
    return render_to_response(go_html,{'testcomments':com_lzllist,'form_login':LoginForm,'form':RegisterForm,'type_id':type,'title_top':title_top,'content':content,'titles':titles_id},RequestContext(request))
    
#访问状态
def Visit(request):
    r10=Redis(host='localhost',port=6379,db=10,password='ffwd')
    r12=Redis(host='localhost',port=6379,db=12,password='ffwd')
    #在线
    online_ipall=[]
    for i in r10.keys('IP*'):
        online_ipall.append((i,r10.get(i)))
    #今天
    today_ipallwx=[]
    for i in r12.keys('IP*'):
        today_ipallwx.append((i,r12.lrange(i,start=0,end=-1)))
    today_ipall=sorted(today_ipallwx,key=lambda x:x[1][1],reverse=True)
    return render_to_response('plug/visit_state.html',{"online_ipall":online_ipall,"today_ipall":today_ipall},RequestContext(request))



#coding=utf8
import time
from redis import Redis
from mydb.models import Blog_inspire


r9=Redis(host='localhost',port=6379,db=9,password='ffwd')
def get_news(keyword):
    titlecurldate=[]
    for i in sorted(r9.lrange(keyword,start=0,end=-1),key=lambda x:eval(x)[2],reverse=True):  #以时间排序
        titlecurldate.append(eval(i))
    return titlecurldate[:20]


def auston_proc(request):
    #主页随机图片
    import random,os
    index_img='hz/'+random.choice(os.listdir('/usr/html/static/img/index/hz'))
    index_list=[('0','学习'),('1','工具'),('2','生活'),('3','标签'),('4','监控'),('5','论坛'),('6','关于')]
    #online redis: key value 过期时间
    if 'HTTP_X_REAL_IP' in request.META:
        ip=request.META['HTTP_X_REAL_IP']
    else:
        ip=request.META['REMOTE_ADDR']
    r10=Redis(host='localhost',port=6379,db=10,password='ffwd')
    r10.setex('IP:'+ip,request.user,60*5)
    online_ips=len(r10.keys('IP*'))
    #励志
    inspires=Blog_inspire.objects.order_by('?')[0].inspire
    #DJANGO 新闻动态  redis: key list
    django_news = get_news('Django')
    #python 新闻动态  redis: key list
    Python_news = get_news('Python')
    #tornado 新闻动态  redis: key list
    Tornado_news = get_news('Tornado')
    Flask_news = get_news('Flask')
    Js_news = get_news('Javascript')
    H5_news = get_news('HTML5')
    Go_news = get_news('Go')
    
    #今日访问
    r12=Redis(host='localhost',port=6379,db=12,password='ffwd')
    now=time.strftime('%Y%m%d %T') 
    refer=request.META.get('HTTP_REFERER','No REFERER')
    r12.ltrim('IP:'+ip,start=10,end=1)  #写入前先清空列表防止叠加
    r12.rpush('IP:'+ip,request.user,now,refer)  #ip命名的列表分别写入 用户、时间、连接来源
    extime=time.mktime(time.strptime(time.strftime('%Y%m%d')+' 23:59:59','%Y%m%d %X'))-time.time()
    r12.expire('IP:'+ip,int(extime))
    today_ips=len(r12.keys('IP*'))

    #all public variables
    return {'list1':index_list,
            'center_img':index_img,
            'url':"http://www.feifeiwd.com", 
            'META':request.META,
            'SESSION':request.session,
            'online_ips':online_ips,
            'User':request.user,
            'inspires':inspires,
            'djangonews':django_news,
            'pythonnews':Python_news,
            'tornadonews':Tornado_news,
            'flasknews':Flask_news,
            'jsnews':Js_news,
            'h5news':H5_news,
            'gonews':Go_news,
            'today_ips':today_ips,
	    'IP':ip,
            }
if __name__ == '__main__':
    django_news = get_news('Django')
    print django_news

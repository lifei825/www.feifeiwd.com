#!/usr/bin/env python
# coding=utf8
import re
import time
import requests
from ffwdsite.ffwdsite.settings import redis_conn
# r9=redis.Redis(host='localhost',port=6379,db=9,password='ffwd')
Url = "https://www.oschina.net/search?q=django&scope=news&days=0&sort_by_time=1"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:42.0) Gecko/20100101 Firefox/42.0',
           'Accept': 'text/html;q=0.9,*/*;q=0.8',
           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
           'Connection': 'close',
           'Referer': 'http://www.oschina.net/search?scope=news&q=python',
           }


class djnew(object):
    r9 = redis_conn(db=9)

    def __init__(self, Url, headers, keyword):
        self.session = requests.Session()
        self.Url = Url
        self.headers = headers
        self.keyword = keyword

    def getweb(self):
        print self.Url
        request = self.session.get(self.Url, headers=self.headers)
        f = request.text
        return f

    def getnew(self):
        webdata = re.sub('''<span class="highlight">%s</span>''' % self.keyword, self.keyword, self.getweb(), flags=re.I)
        newdate = re.findall(u'''发布于 (\d{4}-\d{2}-\d{2})''', webdata, flags=re.S)
        getlist = re.findall(r'''(http[s]{0,1}://.*?.oschina.net/.*?)' target='_blank'>(.*?)</a></h3>''', webdata)
        weblist = []
        n = 0
        for i in getlist:
            url,title=i[0],i[1]
            weblist.append((url,title,newdate[n]));n+=1
        return weblist

    def toredis(self):
        self.r9.delete(self.keyword)
        for url,tit,nd in self.getnew():
            self.r9.rpush(self.keyword,(tit,url,nd))
        #for i in sorted(r9.keys(),key=lambda x:r9.lindex(x,1),reverse=True):
        #    print i,r9.lindex(i,0),r9.lindex(i,1)


if __name__ == '__main__':
    django_new=djnew(Url, headers, 'Django')
    # print django_new.getweb()
    # print "="*50
    # print django_new.getnew()
    django_new.toredis()
    
    Url1 = "http://www.oschina.net/search?q=python&scope=news&days=0&onlytitle=1&sort_by_time=1"
    python_new = djnew(Url1, headers, 'Python')
    # print python_new.getweb()
    python_new.toredis()


    Url2="http://www.oschina.net/search?q=tornado&scope=news&days=0&onlytitle=1&sort_by_time=1"
    tornado_new=djnew(Url2,headers,'Tornado')
    #print tornado_new.getnew()
    tornado_new.toredis()

    Url3="http://www.oschina.net/search?q=flask&scope=news&days=0&onlytitle=1&sort_by_time=1"
    flask_new=djnew(Url3,headers,'Flask')
    flask_new.toredis()
    
    Url4="http://www.oschina.net/search?q=javascript&scope=news&days=0&onlytitle=1&sort_by_time=1"
    js_new=djnew(Url4,headers,'Javascript')
    js_new.toredis()

    Url5="http://www.oschina.net/search?q=html5&scope=news&days=0&onlytitle=1&sort_by_time=1"
    h5_new=djnew(Url5,headers,'HTML5')
    h5_new.toredis()

    Url6="http://www.oschina.net/search?q=go&scope=news&days=0&onlytitle=1&sort_by_time=1"
    go_new=djnew(Url6,headers,'Go')
    go_new.toredis()

#coding=utf-8
from django import template
import re
register=template.Library()

@register.filter('cp')
def tag_cp(x,y):
    return x*y

@register.filter('code')
def tag_code(x):
    xlist=x.split('\n')
    newlist=[];aa=0
    for i in xlist:
        if i.startswith('#fcode'):
            newlist.append(re.sub(i,'<ul style="color:black;border-left:25px solid #ccc;background-color:#AFEEEE;list-style-type:none;">',i))
            aa=1
        elif i.startswith('#ecode'):
            newlist.append(re.sub(i,'</ul>',i))
            aa=0
        elif aa==1:
            li1=re.sub('>','&gt',i)
            li2=re.sub('<','&lt',li1)
            newlist.append('<li>  '+li2)
        # reset url 
        elif i.find('url#') > i.find('#url') > 0:
            href1 = re.sub('#url','<a target="_blank" href="',i)
            href2 = re.sub('url#','">click</a>',href1)
            newlist.append(href2)
        else:
            newlist.append(i)
    return '\n'.join(newlist)

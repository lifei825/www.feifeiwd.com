from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView 
from django.contrib.auth.views import login,logout 
from ffwdsite.contact.views import RegisterView,LoginView,Comment


urlpatterns = patterns('',
    (r'^register/$',RegisterView.as_view()),
    (r'^login/$',LoginView.as_view()),
    (r'^logout/$',logout,{'next_page':'/'}),
    (r'^comment/$',Comment),
    #test
    url(r'^portrait_img/(?P<path>.*.jpg)/$',"django.views.static.serve",{"document_root":"/home/django/ffwdsite/img/portrait_img/"}),
    (r'^wu/$',TemplateView.as_view(template_name="index.html"))
)


urlpatterns += patterns('ffwdsite.views',
    # Examples:
    # url(r'^$', 'ffwdsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^adminstrator/', include(admin.site.urls)),
    (r'^$','Index'),
    (r'^test$','Test'),
    (r'^content/(\d)/(\d+)/$','Content'), 
    (r'^visit/$','Visit'),
)


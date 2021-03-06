from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView 
from django.contrib.auth.views import login,logout 
from contact.views import RegisterView,LoginView,Comment
from api.utils import ChangePicture, Get51News
from . import settings


urlpatterns = patterns('',
    (r'^register/$', RegisterView.as_view()),
    (r'^login/$', LoginView.as_view()),
    (r'^logout/$', logout,{'next_page': '/'}),
    (r'^comment/$', Comment),
    (r'^api/changePicture$', ChangePicture.as_view()),
    (r'^api/get51news$', Get51News.as_view()),
    # test
    url(r'^portrait_img/(?P<path>.*.jpg)/$', "django.views.static.serve", {
        "document_root": settings.BASE_DIR + "/img/portrait_img/"}),
    (r'^wu/$', TemplateView.as_view(template_name="index.html")),
    url(r"^static/(?P<path>.*)$", "django.views.static.serve", {"document_root": settings.STATIC_ROOT}),
)


urlpatterns += patterns('ffwdsite.views',
    # Examples:
    # url(r'^$', 'ffwdsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^adminstrator/', include(admin.site.urls)),
    (r'^$', 'Index'),
    (r'^test$', 'Test'),
    (r'^content/(\d)/(\d+)/$', 'Content'),
    (r'^visit/$', 'Visit'),
    (r'^weibo/$', 'Weibo'),
    (r'^api/click_url$', 'Click_url'),
    (r'^api/click_praise$', 'Click_praise'),
)


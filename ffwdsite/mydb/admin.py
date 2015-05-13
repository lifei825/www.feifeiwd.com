from django.contrib import admin
from mydb.models import Blog_user,Blog_tag,Blog_essay,Blog_comment,Blog_log,Blog_inspire
# Register your models here.
class Choices_comment(admin.StackedInline):
    model=Blog_comment
    extra=1

class Choices_essay(admin.StackedInline):
    model=Blog_essay
    extra=1

class Blog_userAdmin(admin.ModelAdmin):
    #fields=['user','passwd','email','portrait','signature','gender']
    list_display=('id','user','portrait','signature','gender')

class Blog_tagAdmin(admin.ModelAdmin):
    fields=['tag_name']
    inlines=[Choices_essay]

class Blog_essayAdmin(admin.ModelAdmin):
    #fields=['title','content','lastchange','praise','page_view','tag','top']
    fields=['title','content','lastchange','tag','top']
    list_display=('id','title','createtime','lastchange','tag','top','page_view')
    inlines=[Choices_comment]
    date_hierarchy='createtime'

class Blog_commentAdmin(admin.ModelAdmin):
    list_display=('id','blog_essay','comment','comtime','comtype','compraise','blog_user')
    search_fields=['comment']
    list_filter=['comtime']

class Blog_logAdmin(admin.ModelAdmin):
    fields=['action','blog_user']
    list_display=('action','logtime','blog_user')
    search_fields=['action']

class Blog_inspireAdmin(admin.ModelAdmin):
    list_display=('id','inspire',)



admin.site.register(Blog_user,Blog_userAdmin)
admin.site.register(Blog_tag,Blog_tagAdmin)
admin.site.register(Blog_essay,Blog_essayAdmin)
admin.site.register(Blog_comment,Blog_commentAdmin)
admin.site.register(Blog_log,Blog_logAdmin)
admin.site.register(Blog_inspire,Blog_inspireAdmin)

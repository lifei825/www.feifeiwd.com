# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog_comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.CharField(max_length=255, verbose_name=b'\xe8\xaf\x84\xe8\xae\xba')),
                ('comtime', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe7\x95\x99\xe8\xa8\x80\xe6\x97\xb6\xe9\x97\xb4')),
                ('comtype', models.IntegerField(default=0, verbose_name=b'\xe4\xb8\xbb\xe6\xa5\xbcor\xe6\xa5\xbc\xe4\xb8\xad\xe6\xa5\xbc')),
                ('compraise', models.IntegerField(default=0, verbose_name=b'\xe8\xaf\x84\xe8\xae\xba\xe7\x82\xb9\xe8\xb5\x9e')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Blog_essay',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30, verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe5\x90\x8d')),
                ('content', models.TextField(verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe5\x86\x85\xe5\xae\xb9')),
                ('createtime', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4', null=True)),
                ('lastchange', models.DateTimeField(null=True, verbose_name=b'\xe4\xbf\xae\xe6\x94\xb9\xe6\x97\xb6\xe9\x97\xb4', blank=True)),
                ('praise', models.IntegerField(default=0, verbose_name=b'\xe7\x82\xb9\xe8\xb5\x9e')),
                ('page_view', models.IntegerField(default=0, verbose_name=b'\xe6\xb5\x8f\xe8\xa7\x88\xe9\x87\x8f')),
                ('top', models.IntegerField(default=0, verbose_name=b'\xe7\xbd\xae\xe9\xa1\xb6')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Blog_inspire',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('inspire', models.TextField(verbose_name=b'\xe5\x8a\xb1\xe5\xbf\x97\xe5\xbe\xae\xe8\xaf\xad')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Blog_log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('action', models.CharField(max_length=8, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x8a\xa8\xe4\xbd\x9c', choices=[(b'login', b'\xe7\x99\xbb\xe5\xbd\x95'), (b'register', b'\xe6\xb3\xa8\xe5\x86\x8c'), (b'logout', b'\xe7\x99\xbb\xe5\x87\xba')])),
                ('logtime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Blog_tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag_name', models.CharField(unique=True, max_length=20, verbose_name=b'\xe6\xa0\x87\xe7\xad\xbe')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Blog_user',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('portrait', models.ImageField(default=b'portrait_img/user.jpg', upload_to=b'portrait_img/')),
                ('signature', models.CharField(default=b'Say . what..', max_length=20, verbose_name=b'\xe7\xad\xbe\xe5\x90\x8d', blank=True)),
                ('gender', models.CharField(blank=True, max_length=1, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab', choices=[(b'm', b'man'), (b'w', b'woman')])),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='blog_log',
            name='blog_user',
            field=models.ForeignKey(to='mydb.Blog_user'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='blog_essay',
            name='tag',
            field=models.ForeignKey(to='mydb.Blog_tag'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='blog_comment',
            name='blog_essay',
            field=models.ForeignKey(to='mydb.Blog_essay'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='blog_comment',
            name='blog_user',
            field=models.ForeignKey(to='mydb.Blog_user'),
            preserve_default=True,
        ),
    ]

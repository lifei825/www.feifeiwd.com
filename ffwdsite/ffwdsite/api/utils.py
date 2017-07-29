from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View  
import random
import os
import redis
import json
from django.conf import settings


class ChangePicture(View):
    def get(self, request):
        index_img = 'hz/'+random.choice(os.listdir(settings.STATIC_ROOT + '/img/index/hz'))
        print index_img
        return HttpResponse(index_img)


class Get51News(View):
    def get(self, request):
        r9 = redis.Redis(host='127.0.0.1', port=6379, db=9, password='ffwd')
        key = request.GET.get('key')
        data = r9.lrange(key, 0, -1)
        lists = [eval(d) for d in data]
        return HttpResponse(json.dumps(lists), content_type="application/json")


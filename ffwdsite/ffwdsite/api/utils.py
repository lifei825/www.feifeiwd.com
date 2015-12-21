from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View  
import random
import os


class ChangePicture(View):
    def get(self, request):
        index_img = 'hz/'+random.choice(os.listdir('/usr/html/static/img/index/hz'))
        return HttpResponse(index_img)


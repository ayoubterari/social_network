import imp
from django.shortcuts import render
from django.views import View

class Index(View):
    def get(self,request,*arg,**kwargs):
        return render(request,'landing/index.html')
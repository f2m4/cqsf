from django.shortcuts import render,get_object_or_404
from . import models
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    return render(request,'web/index.html')

# # 旧模板页面
# def moban(request):
#     page_num = request.GET.get('page', 1)  # 获取url的页面参数get请求
#     logins=models.LoginTemplates.objects.all()
#     paginator=Paginator(logins,8)
#     page_of_logins=paginator.get_page(page_num)
#     context={}
#     context['page_of_logins']=page_of_logins
#     return render(request,'moban/index.html',context)
#
# def page_one(request,id):
#     page=models.LoginTemplates.objects.get(pk=id)
#     content={}
#     content['page']=page
#     return render(request,'moban/page_login.html',content)
#
# # 新模板页面
# def newmoban(request):
#     page_num = request.GET.get('page', 1)  # 获取url的页面参数get请求
#     logins=models.LoginTemplates.objects.all()
#     paginator=Paginator(logins,8)
#     page_of_logins=paginator.get_page(page_num)
#     context={}
#     context['page_of_logins']=page_of_logins
#     return render(request,'newmoban/index.html',context)
# #登陆器查看页面
# def login_pageone(request,id):
#     context={}
#     context['login']=get_object_or_404(models.LoginTemplates,pk=id)
#     return render(request,'newmoban/login_pageone.html',context)
#
# #nmoban主页
# def nmoban(request):
#     page_num = request.GET.get('page', 1)  # 获取url的页面参数get请求
#     logins=models.LoginTemplates.objects.all()
#     paginator=Paginator(logins,8)
#     page_of_logins=paginator.get_page(page_num)
#     context={}
#     context['page_of_logins']=page_of_logins
#     return render(request,'nmoban/index.html',context)
#
# #登陆器查看页面
# def nlogin_pageone(request,id):
#     context={}
#     context['login']=get_object_or_404(models.LoginTemplates,pk=id)
#     return render(request,'nmoban/login_pageone.html',context)

#统一风格的模板页面
def logint(request):
    page_num = request.GET.get('page', 1)  # 获取url的页面参数get请求
    logins=models.LoginTemplates.objects.all()
    paginator=Paginator(logins,9)
    page_of_logins=paginator.get_page(page_num)
    context={}
    context['page_of_logins']=page_of_logins
    return render(request,'web/logint.html',context)
def logint_pageone(request,id):
    context={}
    context['login']=get_object_or_404(models.LoginTemplates,pk=id)
    return render(request,'web/login_pageone.html',context)
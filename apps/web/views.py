from django.shortcuts import render,get_object_or_404
from . import models
from django.core.paginator import Paginator
# Create your views here.
page_has_number=9
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
    paginator=Paginator(logins,page_has_number)
    page_of_logins=paginator.get_page(page_num)
    #获取当前页面
    current_page=page_of_logins.number
    #获取当前页及前后两页的列表
    page_list=list(range(max(1,current_page-2),current_page))+\
               list(range(current_page,min(paginator.num_pages,current_page+2)+1))
    #添加省略页码
    if current_page-2>2:
        page_list.insert(0,'...')
    if paginator.num_pages-current_page>3:
        page_list.append('...')
    #添加首页和尾页
    if page_list[0]!=1:
        page_list.insert(0,1)
    if page_list[-1]!=paginator.num_pages:
        page_list.append(paginator.num_pages)
    context = {}
    context['page_list']=page_list
    context['page_of_logins']=page_of_logins
    return render(request,'web/logint.html',context)
def logint_pageone(request,id):
    context={}
    detail_login=get_object_or_404(models.LoginTemplates,pk=id)
    context['previous_login']=models.LoginTemplates.objects.filter(cr_date__gt=detail_login.cr_date).last()
    context['next_login'] = models.LoginTemplates.objects.filter(cr_date__lt=detail_login.cr_date).first()
    detail_login.looked_num+=1
    detail_login.save()
    context['login']=detail_login

    return render(request,'web/login_pageone.html',context)

#获取leg,blue类型的登陆器
def login_lb(request):
    page_num = request.GET.get('page', 1)  # 获取url的页面参数get请求
    logins = models.LoginTemplates.objects.filter(sale_price=6)
    paginator = Paginator(logins, page_has_number)
    page_of_logins = paginator.get_page(page_num)
    context = {}

    #获取当前页面
    current_page=page_of_logins.number
    #获取当前页及前后两页的列表
    page_list=list(range(max(1,current_page-2),current_page))+\
               list(range(current_page,min(paginator.num_pages,current_page+2)+1))
    #添加省略页码
    if current_page-2>2:
        page_list.insert(0,'...')
    if paginator.num_pages-current_page>3:
        page_list.append('...')
    #添加首页和尾页
    if page_list[0]!=1:
        page_list.insert(0,1)
    if page_list[-1]!=paginator.num_pages:
        page_list.append(paginator.num_pages)
    context['page_list'] = page_list

    context['page_of_logins'] = page_of_logins
    return render(request, 'web/logint.html', context)
#获取gee,gom,green,hxm类型的登陆器
def login_gh(request):
    page_num = request.GET.get('page', 1)  # 获取url的页面参数get请求
    logins = models.LoginTemplates.objects.filter(sale_price=5)
    paginator = Paginator(logins, page_has_number)
    page_of_logins = paginator.get_page(page_num)
    context = {}

    #获取当前页面
    current_page=page_of_logins.number
    #获取当前页及前后两页的列表
    page_list=list(range(max(1,current_page-2),current_page))+\
               list(range(current_page,min(paginator.num_pages,current_page+2)+1))
    #添加省略页码
    if current_page-2>2:
        page_list.insert(0,'...')
    if paginator.num_pages-current_page>3:
        page_list.append('...')
    #添加首页和尾页
    if page_list[0]!=1:
        page_list.insert(0,1)
    if page_list[-1]!=paginator.num_pages:
        page_list.append(paginator.num_pages)
    context['page_list'] = page_list

    context['page_of_logins'] = page_of_logins
    return render(request, 'web/logint.html', context)
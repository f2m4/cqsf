from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='web_index'),
    # path('moban/',views.moban,name='moban_index'),
    # path('page_login/<int:id>',views.page_one,name='page_login'),
    # path('newmoban/',views.newmoban,name='newmoban'),
    # path('login_page/<int:id>',views.login_pageone,name='login_page'),
    # path('nmoban/',views.nmoban,name='nmoban'),
    # path('nlogin_page/<int:id>',views.nlogin_pageone,name='nlogin_page'),
    path('logint/',views.logint,name='logint'),
    path('logint_page/<int:id>',views.logint_pageone,name='logint_page'),
]
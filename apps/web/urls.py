from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='web_index'),
    path('moban/',views.moban,name='moban_index'),
    path('page_login/<int:id>',views.page_one,name='page_login'),
    path('newmoban/',views.newmoban,name='newmoban'),
]
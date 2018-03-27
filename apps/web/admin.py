from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.SaleType)
class SaleTypeAdmin(admin.ModelAdmin):
    fields = ('title','content','price')
    list_display = ('id','title','content','price')

@admin.register(models.WebTemplates)
class WebTemplatesAdmin(admin.ModelAdmin):
    fields = ('author','title','content','sale_price','saled_num','looked_num')
    list_display = ('id','author','title','content','sale_price','saled_num','looked_num','cr_date','ch_date')

@admin.register(models.LoginTemplates)
class LoginTemplatesAdmin(admin.ModelAdmin):
    fields = ('author','title', 'content', 'pic','sale_price', 'saled_num', 'looked_num')
    list_display = ('id','author','title', 'pic','content', 'sale_price', 'saled_num', 'looked_num', 'cr_date', 'ch_date')
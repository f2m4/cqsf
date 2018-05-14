from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class SaleType(models.Model):
    title = models.CharField('种类',max_length=30)
    content=RichTextUploadingField('说明')
    price=models.IntegerField('价格')

    def __str__(self):
        return self.title

class WebTemplates(models.Model):
    author = models.CharField('作者',max_length=20, default='兵器太邪门')
    title = models.CharField('标题',max_length=30)
    content = RichTextUploadingField('内容')
    sale_price=models.ForeignKey("SaleType",on_delete=models.DO_NOTHING)
    saled_num=models.IntegerField('已售',default=0)
    looked_num=models.IntegerField('查看',default=0)
    cr_date=models.DateTimeField('创建日期',auto_now_add=True)
    ch_date=models.DateTimeField('修改日期',auto_now=True)

    def __str__(self):
        return self.title
    class Meta:
        ordering=['-cr_date']

class LoginTemplates(models.Model):
    author=models.CharField('作者',max_length=20,default='菇凉佳佳佳')
    title = models.CharField('标题',max_length=30)
    pic=models.TextField('图片地址',default='')
    content = RichTextUploadingField('内容')
    sale_price=models.ForeignKey("SaleType",on_delete=models.DO_NOTHING)
    saled_num=models.IntegerField('已售',default=0)
    looked_num=models.IntegerField('查看',default=0)
    cr_date=models.DateTimeField('创建日期',auto_now_add=True)
    ch_date=models.DateTimeField('修改日期',auto_now=True)
    def __str__(self):
        return self.title
    class Meta:
        ordering=['-cr_date']

class SucaiModel(models.Model):
    #作者
    author=models.CharField('作者',max_length=20,default='菇凉佳佳佳')
    #标题
    title=models.CharField('标题',max_length=30)
    #预览图片地址
    pic=models.TextField('图片地址',default='')
    #富文本内容
    content=RichTextUploadingField('内容')
    #价格
    sale_price = models.ForeignKey("SaleType", on_delete=models.DO_NOTHING)
    #已出售的数量
    saled_num = models.IntegerField('已售',default=0)
    #查看的次数
    looked_num = models.IntegerField('查看',default=0)
    #创建日期
    cr_date = models.DateTimeField('创建日期',auto_now_add=True)
    #修改日期
    ch_date = models.DateTimeField('修改日期',auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-cr_date']
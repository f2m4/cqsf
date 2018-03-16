from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class SaleType(models.Model):
    title = models.CharField(max_length=30)
    content=RichTextUploadingField()
    price=models.IntegerField()

    def __str__(self):
        return self.title

class WebTemplates(models.Model):
    title = models.CharField(max_length=30)
    content = RichTextUploadingField()
    sale_price=models.ForeignKey("SaleType",on_delete=models.DO_NOTHING)
    saled_num=models.IntegerField(default=0)
    looked_num=models.IntegerField(default=0)
    cr_date=models.DateTimeField(auto_now_add=True)
    ch_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    class Meta:
        ordering=['-cr_date']

class LoginTemplates(models.Model):
    title = models.CharField(max_length=30)
    pic=models.TextField(default='')
    content = RichTextUploadingField()
    sale_price=models.ForeignKey("SaleType",on_delete=models.DO_NOTHING)
    saled_num=models.IntegerField(default=0)
    looked_num=models.IntegerField(default=0)
    cr_date=models.DateTimeField(auto_now_add=True)
    ch_date=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    class Meta:
        ordering=['-cr_date']


from django.db import models


# Create your models here.

class Category(models.Model):
    code=models.CharField(verbose_name='编号')



class Goods(models.Model):
    barcode=models.CharField(verbose_name='条码')


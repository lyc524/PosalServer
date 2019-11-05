from django.db import models


# Create your models here.

class Category(models.Model):
    code=models.CharField(verbose_name='编号')
    name=models.CharField(verbose_name='类别名称')
    parent_id=models.CharField(verbose_name='父编号')



class Goods(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name='类别ID')
    barcode=models.CharField(verbose_name='条码')
    goods_name=models.CharField(verbose_name='商品名称')
    purchase_price=models.FloatField("进价",default=0)
    sale_price=models.FloatField("售价",default=0)
    profit=models.FloatField("利润",default=0)


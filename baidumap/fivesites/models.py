from django.db import models

# Create your models here.

#场地表
class FiveSite(models.Model):
    sites_name = models.CharField(max_length=200)   #场地名称
    sites_addr = models.CharField(max_length=400)   #场地地址
    sites_avg_price = models.IntegerField(default=0)    #人均价格
    sites_call_phone = models.CharField(max_length=20)  #联系电话
    sites_numbers = models.IntegerField(default=0)  #场地数量
    sites_run_time = models.CharField(max_length=200)   #营业时间
    sites_price = models.CharField(max_length=400)  #场地价格

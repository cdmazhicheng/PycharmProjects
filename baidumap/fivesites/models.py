from django.db import models

# Create your models here.

#场地表
class FiveSite(models.Model):
    sites_name = models.CharField(max_length=200)
    sites_addr = models.CharField(max_length=400)
    sites_avg_price = models.IntegerField(default=0)
    sites_call_phone = models.CharField(max_length=20)
    sites_numbers = models.IntegerField(default=0)
    sites_run_time = models.CharField(max_length=200)
    sites_price = models.CharField(max_length=400)

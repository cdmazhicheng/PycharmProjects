from django.db import models

# Create your models here.

#场地表
class SoccerSite(models.Model):
    soccer_site_name = models.CharField(max_length=200)
    soccer_site_addr = models.CharField(max_length=500)
    soccer_site_linkman = models.CharField(max_length=100)
    soccer_site_mobile = models.CharField(max_length=100)
    soccer_site_star_level = models.IntegerField(default=0)
    soccer_site_create_date = models.DateTimeField
    soccer_site_update_date = models.DateTimeField
    soccer_site_avg_price = models.IntegerField(default=0)

# #场地管理
# class SoccerSiteManager(models.Manager):
#
# #场地查询
# class SoccerSiteQuerySet(models.QuerySet):








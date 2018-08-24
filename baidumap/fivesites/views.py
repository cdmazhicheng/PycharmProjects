from django.shortcuts import render
from django.http import HttpResponse
from .models import FiveSite
import requests
import re
import json

################################################################################
#   index方法作用：                                                            #
#   (1)定义各种场地信息，从数据库获取信息并加工成我们想要的信息；              #
#   (2)通过context 字典将各种信息与index.html 需要展示的字段建立映射关系；     #
################################################################################
def index(request):

    # 成都市地图坐标、百度地图的个人key
    coordinate_chengdu = [104.0723627301342, 30.663315899548743]
    my_ak = 'c3MKSgGnMtYR424l826lqRqIi1cKgGBG'
    #场地的地图坐标和地址
    coordinate_points = []
    fivesite_list_many = list(FiveSite.objects.values_list('sites_addr'))
    fivesite_name_many = list(FiveSite.objects.values_list('sites_name'))
    for i in range(len(fivesite_list_many)):
        urls = 'http://api.map.baidu.com/geocoder/v2/?output=json&ak={}&address={}'.format(my_ak, fivesite_list_many[i])
        url_requests = requests.get(urls)
        result_points = url_requests.text
        lngs = re.search('\d.{15}', re.search('"lng":.*,"lat"', result_points).group()).group()
        lats = re.search('\d.{15}', re.search('"lat":.*},"precise"', result_points).group()).group()
        coordinate_alone = (lngs, lats)
        coordinate_points.append(coordinate_alone)
    #场地详细信息（人均消费、联系电话、场地数量、营业时间、场地价格）
    fivesite_list_price_avg = list(FiveSite.objects.values_list('sites_avg_price'))
    fivesite_call_phone = list(FiveSite.objects.values_list('sites_call_phone'))
    fivesite_numbers = list(FiveSite.objects.values_list('sites_numbers'))
    fivesite_run_time = list(FiveSite.objects.values_list('sites_run_time'))
    fivesite_site_price = list(FiveSite.objects.values_list('sites_price'))
    fivesite_sum_result = list(zip(fivesite_list_price_avg, fivesite_call_phone, fivesite_numbers, fivesite_run_time, fivesite_site_price ))

    context = {
        #成都市地图坐标、百度地图的个人key
        'coordinate_chengdu': coordinate_chengdu,
        'my_ak': my_ak,
        #场地的地图坐标和地址
        'coordinate_points': json.dumps(coordinate_points),
        'fivesite_name_many': json.dumps(fivesite_name_many, ensure_ascii=False),
        #场地详细信息（人均消费、联系电话、场地数量、营业时间、场地价格）
        'fivesite_sum_result': json.dumps(fivesite_sum_result, ensure_ascii=False),
    }

    return render(request, 'index.html', context)

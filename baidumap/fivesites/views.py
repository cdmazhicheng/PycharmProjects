from django.shortcuts import render
from django.http import HttpResponse
from .models import FiveSite
import requests
import re
import json

# Create your views here.
def index(request):

    #基础数据
    coordinate_chengdu = [104.0723627301342, 30.663315899548743]
    my_ak = 'c3MKSgGnMtYR424l826lqRqIi1cKgGBG'

    #单地址
    # fivesite_list_only = FiveSite.objects.get(id=1).sites_addr  #获取地址
    # url = 'http://api.map.baidu.com/geocoder/v2/?output=json&ak={}&address={}'.format(my_ak, fivesite_list_only)
    # url_request = requests.get(url)
    # result_test = url_request.text
    # lng =re.search( '\d.{15}',re.search('"lng":.*,"lat"',result_test).group()).group()
    # lat = re.search('\d.{15}', re.search('"lat":.*},"precise"', result_test).group()).group()
    # coordinate_point = (lng, lat)
    # fivesit_name_only = FiveSite.objects.get(id=1).sites_name

    #多地址
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

    context = {
        #基础数据
        'coordinate_chengdu': coordinate_chengdu,
        'my_ak': my_ak,

        #单地址
        # 'coordinate_point': coordinate_point,
        # 'fivesit_name_only': fivesit_name_only,

        #多地址
        'coordinate_points': json.dumps(coordinate_points),
        'fivesite_name_many': json.dumps(fivesite_name_many, ensure_ascii=False),
    }

    return render(request, 'index.html', context)

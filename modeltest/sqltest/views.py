from django.shortcuts import render
from .models import SoccerSite
import requests
import re
import json

# Create your views here.

def display(request):
    #基础数据
    coordinate_chengdu = [104.0723627301342,30.663315899548743]
    my_ak = 'c3MKSgGnMtYR424l826lqRqIi1cKgGBG'
    coordinate_points = []

    #sqltest内容
    testbegin = "测试数据......"
    soccersite_list = SoccerSite.objects.get(id=1).soccer_site_addr   #单地址
    soccersite_list_points = list(SoccerSite.objects.values_list('soccer_site_addr'))   #多地址

    #map接口
    url = 'http://api.map.baidu.com/geocoder/v2/?output=json&ak={}&address={}'.format(my_ak, soccersite_list)
    url_request = requests.get(url)
    result_test = url_request.text
    lng =re.search( '\d.{15}',re.search('"lng":.*,"lat"',result_test).group()).group()
    lat = re.search('\d.{15}', re.search('"lat":.*},"precise"', result_test).group()).group()
    coordinate_point = (lng, lat)

    #多pointmap接口
    for i in range(len(soccersite_list_points)):
        urls = 'http://api.map.baidu.com/geocoder/v2/?output=json&ak={}&address={}'.format(my_ak, soccersite_list_points[i])
        url_requests = requests.get(urls)
        result_points = url_requests.text
        lngs = re.search('\d.{15}', re.search('"lng":.*,"lat"', result_points).group()).group()
        lats = re.search('\d.{15}', re.search('"lat":.*},"precise"', result_points).group()).group()
        coordinate_alone = (lngs, lats)
        coordinate_points.append(coordinate_alone)

    context= {
        #基础数据
        'coordinate_chengdu': coordinate_chengdu,
        'my_ak': my_ak,

        # sqltest内容
        'testbegin':testbegin,
        'soccersite_list': soccersite_list,

        #map接口
        # 'result_test': result_test,
        'coordinate_point': coordinate_point,
        'coordinate_points': json.dumps(coordinate_points),


    }

    return render(request,'displayweb.html',context)

from django.shortcuts import render
from .models import SoccerSite
import requests
import re

# Create your views here.

def display(request):
    #基础数据
    coordinate_chengdu = [104.0723627301342,30.663315899548743]
    my_ak = 'c3MKSgGnMtYR424l826lqRqIi1cKgGBG'

    #sqltest内容
    testbegin = "测试数据......"
    soccersite_list = SoccerSite.objects.get(id=1).soccer_site_addr
    soccersite_list_test = SoccerSite.objects.values_list('soccer_site_addr')

    #map接口
    url = 'http://api.map.baidu.com/geocoder/v2/?output=json&ak={}&address={}'.format(my_ak, soccersite_list)
    url_request = requests.get(url)
    result_test = url_request.text
    lng =re.search( '\d.{15}',re.search('"lng":.*,"lat"',result_test).group()).group()
    lat = re.search('\d.{15}', re.search('"lat":.*},"precise"', result_test).group()).group()


    context= {
        #基础数据
        'coordinate_chengdu': coordinate_chengdu,
        'my_ak': my_ak,

        # sqltest内容
        'testbegin':testbegin,
        'soccersite_list': soccersite_list,
        'soccersite_list_test': soccersite_list_test,

        #map接口
        # 'result_test': result_test,
        'lng': lng,
        'lat': lat,

    }

    return render(request,'displayweb.html',context)

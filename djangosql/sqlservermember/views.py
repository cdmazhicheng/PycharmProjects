from django.shortcuts import render
from sqlserveruser.calltables import user_table, coupon_table, order_table
import time
from . import models
from django.http import HttpResponse
from sqlserveruser import models

#账号数据
def member(request):

    context = {
               #本地数据库账号
               }

    return render(request, 'sqlservertester/member.html', context)

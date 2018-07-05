from django.shortcuts import render
from sqlservermember.calltables import kanban
import time
from . import models
from django.http import HttpResponse
from sqlserveruser import models

def member(request):

#######注册用户##########

    #时间区间注册数据
    pit_member_user_register = kanban.pit_member_user_register(request)[0][0]
    begin_time = kanban.begin_time
    end_time = kanban.end_time
    # #当天注册数据
    # pit_member_user_register_today = 3
    # #昨日注册数据
    # pit_member_user_register_yesterday = 5
    #当天注册数据
    pit_member_user_register_today = kanban.pit_member_user_register_today(request)[0][0]
    #昨日注册数据
    pit_member_user_register_yesterday = kanban.pit_member_user_register_yesterday(request)[0][0]
    #注册人数同比增长
    if pit_member_user_register_yesterday == 0:
        register_ratio = pit_member_user_register_today
    elif pit_member_user_register_today == 0:
        register_ratio = -pit_member_user_register_yesterday
    else:
        register_ratio = pit_member_user_register_today/pit_member_user_register_yesterday

#######新增会员##########

    # 新增会员数量
    pit_member_user_vip = kanban.pit_member_user_vip(request)[0][0]
    #今日会员数量
    pit_member_user_vip_today = kanban.pit_member_user_vip_today(request)[0][0]
    #昨日会员数量
    pit_member_user_vip_yesterday = kanban.pit_member_user_vip_yesterday(request)[0][0]
    #会员同比增长
    if pit_member_user_vip_today == 0:
        vip_ratio = pit_member_user_vip_today
    elif pit_member_user_vip_yesterday == 0:
        vip_ratio = -pit_member_user_vip_yesterday
    else:
        vip_ratio = pit_member_user_vip_today / pit_member_user_vip_yesterday

#######会员支付人数##########

        #时间区间会员支付人数
        pit_member_user_pay_number = len(kanban.pit_member_user_pay_number(request))
        #今日会员支付人数
        pit_member_user_pay_number_today = len(kanban.pit_member_user_pay_number_today(request))
        #昨日会员支付人数
        pit_member_user_pay_number_yesterday = len(kanban.pit_member_user_pay_number_yesterday(request))
        #会员同比增长
        if pit_member_user_pay_number_today == 0:
            pay_number_ratio = pit_member_user_pay_number_today
        elif pit_member_user_pay_number_yesterday == 0:
            pay_number_ratio = -pit_member_user_pay_number_yesterday
        else:
            pay_number_ratio = round(pit_member_user_pay_number_today / pit_member_user_pay_number_yesterday, 2)


####################
##  context部分 ####
####################


    context = {

#######注册用户##########

               #时间区间注册数据
                'pit_member_user_register': pit_member_user_register,
                'begin_time': begin_time,
                'end_time': end_time,
                #当天注册数据
                'pit_member_user_register_today': pit_member_user_register_today,
                # 昨日注册数据
                'pit_member_user_register_yesterday': pit_member_user_register_yesterday,
                # 注册人数同比增长
                'register_ratio': register_ratio,

#######新增会员##########

                # 新增会员数量
                'pit_member_user_vip': pit_member_user_vip,
                'pit_member_user_vip_today': pit_member_user_vip_today,
                'pit_member_user_vip_yesterday': pit_member_user_vip_yesterday,
                'vip_ratio': vip_ratio,

#######会员支付人数##########

                'pit_member_user_pay_number': pit_member_user_pay_number,
                'pit_member_user_pay_number_today': pit_member_user_pay_number_today,
                'pit_member_user_pay_number_yesterday': pit_member_user_pay_number_yesterday,
                'pay_number_ratio': pay_number_ratio,

               }

    return render(request, 'sqlservertester/member.html', context)

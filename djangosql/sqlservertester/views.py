from django.shortcuts import render
from sqlservertester.calltables import user_table


def user(request):

    message_user = user_table.user_message(request) #pit_member_user表
    member_sms = user_table.member_user(request)#pit_member_sms表
    wechat_user = user_table.wechat_user(request)  # pit_wechat_user表

    context = {'user_id': message_user[0][0],
               'suggest_user_id': message_user[0][1],
               'nickname': message_user[0][2],
               'mobile': message_user[0][3],
               'member_sms': member_sms[0][0],
               'wechat_user': wechat_user[0][0],
               }

    return render(request, 'sqlservertester/home.html', context)
